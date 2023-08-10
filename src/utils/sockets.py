import time
import jsons
import zmq
from classes.board import Board
from classes.cell import Cell
from classes.move import Move
from events.step import doMove, stepWithCount
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
                    app.socket.send_string("ACK-GET-BOARD")
                    boardJson = jsons.dumps(app.board, strip_privates=True)
                    app.socket.send_string(boardJson)
                    print(f"! Sent board to secondary node: {boardJson}")
                case "ACK-GET-BOARD":
                    app.lock.acquire()
                    print("RRRacquire")

                    boardJson = app.socket.recv_string()
                    print(f"! Received board from primary node: {boardJson}")
                    board = jsons.loads(boardJson, Board)
                    for r in range(len(board.grid)):
                        for c in range(len(board.grid[r])):
                            jsonStr = jsons.dumps(board.grid[r][c])
                            board.grid[r][c] = jsons.loads(jsonStr, Cell)
                            board.grid[r][c].setup(app)
                    app.board = board
                    app.board.setup(app, False)

                    app.lock.release()
                    print("RRRrelease")
                case "STEP-1":
                    for _ in range(app.stepsPerSecond * 2):
                        stepWithCount(app)
                case "STEP-25":
                    for _ in range(app.stepsPerSecond * 25 * 2):
                        stepWithCount(app)
                case "MOVE":
                    split = msg.split(" ")
                    playerId = int(split[1])
                    x = int(split[2])
                    y = int(split[3])
                    doMove(playerId, app, Move((x, y)))
        except zmq.Again:
            continue


def sendMessages(app):
    """Send messages to the socket."""

    while not app.stopEvent.is_set():
        # delay otherwise it'll use a ton of cpu
        time.sleep(0.5)

        msg = app.msg
        if msg is None:
            continue

        # modify app inside the mutex
        app.lock.acquire()
        print("SSSacquire")
        app.msg = None
        app.release()
        app.socket.send_string(msg)

        print(f"sent: {msg}", flush=True)

        if msg == "EXIT":
            print("! Exiting...", flush=True)
            app.socket.send("DISCONNECTED".encode("utf-8"))
            app.stopEvent.set()
            app.socket.close()
            break
        app.lock.release()
        print("SSSrelease")


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
