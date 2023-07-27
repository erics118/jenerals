from cmu_graphics import *
from objects.board import drawBoard, Board
from events.keyPress import keyPress
from events.mousePress import mousePress
from events.step import step


def onAppStart(app):
    app.stepsPerSecond = 2

    app.board = Board(20, 20)

    app.cellBorderWidth = 1

    app.selectedCoords = (0, 0)
    app.premoveSelectedCoords = (0, 0)
    app.isFocused = True

    app.flag = False

    app.premoves = []

    app.c = 0


def redrawAll(app):
    drawBoard(app)


def onKeyPress(app, key):
    keyPress(app, key)


def onMousePress(app, mouseX, mouseY):
    mousePress(app, mouseX, mouseY)


def onStep(app):
    step(app)


runApp(width=600, height=600)
