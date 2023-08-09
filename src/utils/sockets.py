import pickle
import time
import zmq
from classes.move import Move
from events.step import doMove
from utils.ip import decodeIp, getLocalIp


def recvMessages(app):
    """Receive messages from the socket."""

    while not app.stopEvent.is_set():
        try:
            msg = app.socket.recv_string(flags=zmq.NOBLOCK)
            command = msg.split(" ")[0]

            match command:
                case "PING":
                    app.socket.send_string("PONG")
                case "CONNECTED":
                    print("! A secondary node has connected to this primary.")
                    app.socket.send_string("ACK-CONNECTED")
                case "ACK-CONNECTED":
                    print("! Connected to a primary node.")
                case "DISCONNECTED":
                    print("! Another node has disconnected from this node.")
                    app.stopEvent.set()
                    app.socket.close()
                case "GET-BOARD":
                    print("trying to send board")
                    app.socket.send_string("ACK-GET-BOARD")
                    # TODO: implement board serialization and deserialization
                    # because pickle doesn't work with things outside
                    # of its own module
                    app.socket.send_pyobj(app.board, protocol=pickle.HIGHEST_PROTOCOL)
                case "ACK-GET-BOARD":
                    app.board = app.socket.recv_pyobj()
                case "MOVE":
                    split = msg.split(" ")
                    playerId = int(split[1])
                    x = int(split[2])
                    y = int(split[3])
                    print(f"received move: {playerId}, ({x}, {y})")
                    doMove(playerId, app, Move((x, y)))
                case _:
                    print(">", msg)
        except zmq.Again:
            continue


def sendMessages(app):
    """Send messages to the socket."""

    while not app.stopEvent.is_set():
        # delay otherwise it'll use a ton of cpu
        time.sleep(0.05)

        msg = app.msg.get()
        if msg is None:
            continue
        app.msg.clear()

        app.socket.send_string(msg)

        print(f"sent: {msg}", flush=True)

        if msg == "EXIT":
            print("! Exiting...", flush=True)
            app.socket.send("DISCONNECTED".encode("utf-8"))
            app.stopEvent.set()
            app.socket.close()
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
