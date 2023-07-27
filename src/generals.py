from cmu_graphics import *
from objects.board import drawBoard, generateBoard
from events.mousePress import mousePress
from events.keyPress import keyPress


def onAppStart(app):
    app.stepsPerSecond = 30

    # grid constants
    app.rows = 20
    app.cols = 20
    app.boardLeft = 50
    app.boardTop = 50
    app.boardWidth = 500
    app.boardHeight = 500
    app.cellBorderWidth = 1

    app.cellWidth = app.boardWidth / app.cols
    app.cellHeight = app.boardHeight / app.rows

    # [[None] * app.cols for _ in range(app.rows)]
    generateBoard(app)

    app.selectedCell = (0, 0)
    app.isFocused = True

    app.flag = False


def onStep(app):

    print(app.selectedCell)


def redrawAll(app):
    drawBoard(app)


def onMousePress(app, mouseX, mouseY):
    mousePress(app, mouseX, mouseY)


def onKeyPress(app, key):
    keyPress(app, key)

runApp(width=600, height=600)
