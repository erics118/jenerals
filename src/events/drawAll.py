from cmu_graphics import *

from classes.board import drawBoard
from objects.background import drawBackground
from objects.game import drawGame
from objects.startScreen import drawStartScreen


def drawAll(app):
    """Draw all elements of the app"""

    drawBackground(app)

    if not app.hasOngoingGame:
        drawStartScreen(app)
    else:
        drawGame(app)

    if app.flag:
        drawRect(10, 10, 30, 30, fill="red")

    for button in app.buttons:
        button.draw()
