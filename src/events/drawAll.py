from cmu_graphics import *

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

    for _, button in app.buttons.items():
        button.draw()
