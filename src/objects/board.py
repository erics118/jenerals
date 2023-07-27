from .border import drawBoardBorder
from .cell import drawBoardCells, Cell
from cmu_graphics import *


def generateBoard(app):
    app.board = makeList(app.rows, app.cols)

    for r in range(app.rows):
        for c in range(app.cols):
            app.board[r][c] = Cell(r, c, "neutral", "fog", 0)

    # put general in the top left
    app.board[0][0] = Cell(0, 0, "player", "general", 1)


def drawBoard(app):
    drawBoardCells(app)
    drawBoardBorder(app)
