from .border import drawBoardBorder
from .cell import drawBoardCells


def drawBoard(app):
    drawBoardCells(app)
    drawBoardBorder(app)
