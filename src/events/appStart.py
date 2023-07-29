from classes.board import Board


def newGame(app):
    """Create a new game"""

    app.hasOngoingGame = True
    app.isDragging = False
    app.isPaused = False
    app.forceIsVisible = False

    app.mx = 0
    app.my = 0

    app.stepsPerSecond = 2

    app.board = Board(app, 20, 20)

    app.cellBorderWidth = 1

    app.isFocused = True

    app.premoves = []

    app.c = 0


def appStart(app, dev):
    # is developer mode flag
    app.dev = dev

    # used to check something is working while developing
    app.flag = False

    app.hasOngoingGame = False

    # lambda to add a function to the app
    app.startGame = lambda: newGame(app)
