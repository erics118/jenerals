from objects.board import drawBoard
from cmu_graphics import *
import utils.colors as colors


def drawBackground(app):
    drawRect(0, 0, app.width, app.height, fill=colors.BACKGROUND)


def drawTurnCounter(app):
    w = 70
    h = 20
    borderWidth = 3
    drawRect(0, 0, w + borderWidth, h + borderWidth, fill=colors.ACCENT)
    drawRect(0, 0, w, h, fill=colors.WHITE)
    label = f"Turn {app.c//2}"
    if app.c % 2 == 1:
        label += "."
    drawLabel(label, w // 2, h // 2, size=14, fill=colors.BLACK, align="center")


def drawAll(app):
    drawBackground(app)

    drawBoard(app)

    drawTurnCounter(app)

    if app.flag:
        drawRect(10, 10, 30, 30, fill="red")
