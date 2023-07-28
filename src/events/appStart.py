from objects.board import Board


def appStart(app):
    app.isPaused = False
    app.forceIsVisible = False

    app.mx = 0
    app.my = 0

    app.stepsPerSecond = 2

    app.board = Board(20, 20)

    app.cellBorderWidth = 1

    app.selectedCoords = (0, 0)
    app.premoveSelectedCoords = (0, 0)
    app.isFocused = True

    app.flag = False

    app.premoves = []

    app.c = 0
