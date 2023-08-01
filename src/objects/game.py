from cmu_graphics import *

from classes.board import drawBoard
from objects.premoves import drawPremoves
from objects.turnCounter import drawTurnCounter


def drawGame(app):
    """Draw the game"""

    drawBoard(app)
    drawPremoves(app)
    drawTurnCounter(app)
