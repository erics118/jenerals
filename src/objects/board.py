from .border import drawBoardBorder
from .cell import drawBoardCells, Cell
from cmu_graphics import *
import random


def randomCellType():
    r = random.randint(0, 99)
    if r < 15:
        return "mountain"
    elif r < 20:
        return "city"
    else:
        return "fog"


class Board:
    def __init__(self, rows, cols):
        # static board properties
        self.rows = rows
        self.cols = cols

        self.left = 50
        self.top = 50
        self.width = 500
        self.height = 500

        self.cellWidth = self.width / self.cols
        self.cellHeight = self.height / self.rows

        # the grid
        self.grid = makeList(rows, cols)

        # set them all to be blank
        # TODO: randomly add cities and mountains
        # TODO: make sure there are no blocked areas
        # maybe by seeing if flood fill can reach all cells
        for r in range(rows):
            for c in range(cols):
                self.grid[r][c] = Cell(r, c, "neutral", randomCellType())

        # put player's general in the top left
        # TODO: put into random place
        self.grid[0][0] = Cell(0, 0, "player", "general")

    # helper function to get the cell at a row and col
    def at(self, row, col):
        r = min(max(row, 0), self.rows - 1)
        c = min(max(col, 0), self.cols - 1)

        return self.grid[r][c]

    # increment cells
    def step(self, mode):
        if mode == "city":
            for r in range(self.rows):
                for c in range(self.cols):
                    # if is a city or general
                    if (
                        self.grid[r][c].t in ["city", "general"]
                        and self.grid[r][c].team != "neutral"
                    ):
                        self.grid[r][c].numTroops += 1
        if mode == "all":
            for r in range(self.rows):
                for c in range(self.cols):
                    self.grid[r][c].step()


def drawBoard(app):
    drawBoardCells(app)
    drawBoardBorder(app)
