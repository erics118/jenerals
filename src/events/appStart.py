import threading
import time
from cmu_graphics import *
from classes.board import Board

from classes.button import Button
from classes.player import Player
from utils.colors import Colors
from utils.image import loadImages
from utils.sockets import recvMessages, sendMessages


def newGame(app):
    """Create a new game"""

    app.buttons["play"].drawing = False
    app.buttons["replay"].drawing = False
    app.buttons["exit"].drawing = False

    app.hasOngoingGame = True
    app.isPaused = False
    app.ended = False
    app.winnerId = None

    app.forceIsVisible = False

    app.mouseCoords = None

    app.players = [
        Player(0, "blue bruh", Colors.BLUE),
        Player(1, "red bro", Colors.RED),
    ]

    if app.identity == 0:
        app.board = Board()
        app.board.setup(app, True)
        app.board.step("city")
    else:  # app.identity == 1:
        app.board = Board()
        app.msg = "GET-BOARD"

    # start at first turn
    app.c = 1 * app.stepsPerSecond

    # wait for the board to be received and setup
    time.sleep(1)


def appStart(app, socket, ip, identity, dev):
    """Start the app"""

    # MUTEX WORK TY GLEB
    app.lock = threading.Lock()
    # is developer mode flag
    app.dev = dev
    app.ip = ip
    app.socket = socket
    app.identity = identity
    app.msg = None
    app.stopEvent = threading.Event()

    # static values
    app.width = 800
    app.height = 800
    app.stepsPerSecond = 2
    app.cellBorderWidth = 0.8

    # used to check something is working while developing
    app.flag = False

    # dragging
    app.isDragging = False

    # game
    app.hasOngoingGame = False
    app.cellSize = 32

    # buttons
    app.pressedButtonName = None

    def goToStartScreen(app):
        app.hasOngoingGame = False
        app.buttons["play"].drawing = True
        app.buttons["replay"].drawing = False
        app.buttons["exit"].drawing = False

    app.buttons = {
        "play": Button(
            400,
            440,
            170,
            60,
            text="Play",
            onClick=newGame,
            textColor=Colors.ACCENT,
            textSize=22,
        ),
        "replay": Button(
            400,
            400,
            140,
            50,
            text="Replay",
            onClick=newGame,
            textColor=Colors.WHITE,
            textSize=18,
            fill=Colors.ACCENT,
            accent=Colors.BACKGROUND,
            drawing=False,
        ),
        "exit": Button(
            400,
            470,
            140,
            50,
            text="Exit",
            onClick=goToStartScreen,
            textColor=Colors.WHITE,
            textSize=18,
            fill=Colors.ACCENT,
            accent=Colors.BACKGROUND,
            drawing=False,
        ),
    }

    # load all images, for visible and not visible
    loadImages(app)

    # create threads for listening and sending messages
    threading.Thread(target=sendMessages, args=(app,)).start()
    threading.Thread(target=recvMessages, args=(app,)).start()
