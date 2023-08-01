from cmu_graphics import *

from classes.board import Board


def newGame(app):
    """Create a new game"""

    app.hasOngoingGame = True
    app.isPaused = False
    app.forceIsVisible = False

    app.mouseCoords = None

    app.board = Board(app, 20, 20)

    app.isFocused = True

    app.premoves = []

    app.c = 0


def appStart(app, dev):
    """Start the app"""

    # static values
    app.width = 800
    app.height = 800
    app.stepsPerSecond = 2
    app.cellBorderWidth = 0.8

    # is developer mode flag
    app.dev = dev

    # used to check something is working while developing
    app.flag = False

    # dragging
    app.isDragging = False

    # buttons
    app.pressedButtonId = None
    app.buttons = []

    # game
    app.hasOngoingGame = False

    # lambda to add a start the game
    app.startGame = lambda: newGame(app)
