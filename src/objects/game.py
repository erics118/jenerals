from cmu_graphics import *

from objects.premoves import drawPremoves
from objects.turnCounter import drawTurnCounter


def drawGame(app):
    """Draw the game"""

    app.board.draw()
    drawPremoves(app)
    drawTurnCounter(app)
