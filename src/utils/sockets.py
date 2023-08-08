import zmq
from classes.move import Move
from events.step import doMove
from utils.ip import decodeIp, getLocalIp


def recvMessages(app, socket):
    """Receive messages from the socket."""

    while not app.stopEvent.is_set():
        try:
            msg = socket.recv_string(flags=zmq.NOBLOCK)
            command = msg.split(" ")[0]

            match command:
                case "PING":
                    socket.send_string("PONG")
                case "CONNECTED":
                    print("! A secondary node has connected to this primary.")
                    socket.send_string("ACK-CONNECTED")
                case "ACK-CONNECTED":
                    print("! Connected to a primary node.")
                case "DISCONNECTED":
                    print("! Another node has disconnected from this node.")
                    app.stopEvent.set()
                    socket.close()
                case "MOVE":
                    split = msg.split(" ")
                    playerId = int(split[1])
                    x = int(split[2])
                    y = int(split[3])
                    doMove(playerId, app, Move(app.board.at((x, y))))
                case _:
                    print(">", msg)
        except zmq.Again:
            continue


def sendMessages(app, socket):
    """Send messages to the socket."""

    if app.msg is None:
        return

    msg = app.msg
    app.msg = None

    while not app.stopEvent.is_set():
        # msg = input("")
        # need this check bc input() doesn't check it
        if app.stopEvent.is_set():
            break
        socket.send_string(msg)
        if msg == "EXIT":
            print("! Exiting...")
            socket.send("DISCONNECTED".encode("utf-8"))
            app.stopEvent.set()
            socket.close()
            break


def makeSocket():
    """Create a socket."""

    context = zmq.Context()
    socket = context.socket(zmq.DEALER)
    return socket


def makePrimarySocket():
    """Create a socket and bind it to a port."""

    ip = getLocalIp()

    socket = makeSocket()
    socket.setsockopt(zmq.IDENTITY, b"0")
    socket.bind("tcp://*:5555")
    return (socket, ip, 0)


def makeSecondarySocket(code):
    """Create a socket and connect it to a port."""

    ip = decodeIp(code)

    socket = makeSocket()
    socket.setsockopt(zmq.IDENTITY, b"1")
    socket.connect(f"tcp://{ip}:5555")
    socket.send("CONNECTED".encode("utf-8"))
    return (socket, ip, 1)
