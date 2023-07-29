from utils.floodFill import floodFill
from .border import drawBoardBorder
from .cell import drawBoardCells, Cell
from cmu_graphics import *
import random


def _randomCellType():
    r = random.randint(0, 99)
    if r < 15:
        return "mountain"
    elif r < 20:
        return "city"
    else:
        return "fog"


def _randomCoords(rows, cols):
    return (random.randint(0, rows - 1), random.randint(0, cols - 1))


def _generateGrid(rows, cols):
    grid = makeList(rows, cols)

    for r in range(rows):
        for c in range(cols):
            grid[r][c] = Cell(r, c, "neutral", _randomCellType())

    # put player's jeneral in the top left
    # TODO: put in a random place, at least rows//2 away from the opponent
    r, c = _randomCoords(rows, cols)
    grid[r][c] = Cell(r, c, "player", "jeneral")
    grid[r][c].isVisible = True
    return (grid, (r, c))


def _hasBlockedAreas(grid):
    rows = len(grid)
    cols = len(grid[0])

    # 0 is unvisited
    # 1 is blocked
    # 2 is visited
    tempGrid = makeList(rows, cols)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c].t == "mountain" or grid[r][c] == "city":
                tempGrid[r][c] = 1
            else:
                tempGrid[r][c] = 0

    # flood fill, making visited cells 2
    floodFill(tempGrid)

    # true if there are any 0's, meaning unvisited cells
    return any(0 in r for r in tempGrid)


class Board:
    def __init__(self, app, rows, cols):
        # static board properties
        self.rows = rows
        self.cols = cols

        self.left = 50
        self.top = 50
        self.width = 500
        self.height = 500

        self.cellWidth = self.width / self.cols
        self.cellHeight = self.height / self.rows

        # randomly generate the grid
        self.grid, jeneralCoords = _generateGrid(self.rows, self.cols)

        # regenerate grid until there are no blocked areas
        while _hasBlockedAreas(self.grid):
            self.grid, jeneralCoords = _generateGrid(self.rows, self.cols)

        app.selectedCoords = jeneralCoords
        app.premoveSelectedCoords = jeneralCoords

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
                    # if is a city or jeneral
                    if (
                        self.grid[r][c].t in ["city", "jeneral"]
                        and self.grid[r][c].team != "neutral"
                    ):
                        self.grid[r][c].numTroops += 1

        if mode == "all":
            for r in range(self.rows):
                for c in range(self.cols):
                    self.grid[r][c].step()

    # collect all troops into a single cell
    def collectTroops(self, coords):
        cnt = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c].team == "player":
                    if (r, c) == coords:
                        continue
                    if self.grid[r][c].numTroops > 1:
                        cnt += self.grid[r][c].numTroops - 1
                        self.grid[r][c].numTroops = 1
        self.grid[coords[0]][coords[1]].numTroops += cnt


def drawBoard(app):
    drawBoardCells(app)
    drawBoardBorder(app)
