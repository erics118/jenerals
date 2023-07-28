from objects.board import drawBoard
from cmu_graphics import *
import utils.colors as colors


def drawBackground(app):
    drawRect(0, 0, app.width, app.height, fill=colors.BACKGROUND)


def drawTurnCounter(app):
    w = 75
    h = 20
    borderWidth = 3

    # draw the outer rect for accent color
    drawRect(0, 0, w + borderWidth, h + borderWidth, fill=colors.ACCENT)

    # draw the inner rect for white
    drawRect(0, 0, w, h, fill=colors.WHITE)

    # create the label
    # show a `.` after the turn if it is 
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
