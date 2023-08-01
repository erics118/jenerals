from cmu_graphics import *

from classes.board import Board


def newGame(app):
    """Create a new game"""

    app.hasOngoingGame = True
    app.isPaused = False
    app.forceIsVisible = False

    app.mouseCoords = None

    app.stepsPerSecond = 2

    app.board = Board(app, 20, 20)

    app.cellBorderWidth = 0.8

    app.isFocused = True

    app.premoves = []

    app.c = 0


def appStart(app, dev):
    app.width = 800
    app.height = 800
    """Start the app"""

    # is developer mode flag
    app.dev = dev
    app.isDragging = False

    app.pressedButtonId = None

    # used to check something is working while developing
    app.flag = False

    app.hasOngoingGame = False

    # lambda to add a function to the app
    app.startGame = lambda: newGame(app)

    # def f(app):
    #     app.flag ^= True

    app.buttons = [
        # Button(
        #     50,
        #     50,
        #     100,
        #     100,
        #     fill=rgb(230, 200, 200),
        #     onClick=f,
        #     borderWidth=3,
        #     borderColor=rgb(200, 100, 100),
        #     text="hi",
        #     textColor="red",
        # )
    ]
