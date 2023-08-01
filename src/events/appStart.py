from cmu_graphics import *

from classes.board import Board
from classes.button import Button
from utils.colors import Colors


def newGame(app):
    """Create a new game"""

    app.buttons["play"].drawing = False

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

    # game
    app.hasOngoingGame = False

    # buttons
    app.pressedButtonName = None

    app.buttons = {
        "play": Button(
            400,
            440,
            170,
            60,
            text="PLAY",
            onClick=newGame,
            textColor=Colors.ACCENT,
            textSize=22,
        )
    }
