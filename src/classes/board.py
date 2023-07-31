from random import randint

from cmu_graphics import *

from utils.floodFill import floodFill

from .border import drawBoardBorder
from .cell import Cell, drawCell


def randomCellType():
    """Generate a random cell type, with hardcoded probabilities"""

    r = randint(0, 99)

    if r < 15:
        return "mountain"

    if r < 20:
        return "city"

    return "fog"


def randomCoords(rows, cols):
    """Generate a random coordinate"""

    return (randint(0, rows - 1), randint(0, cols - 1))


def generateGrid(rows, cols):
    """
    Generate a random grid

    Returns the grid and the coordinates of the general
    The general is the starting selected cell
    """

    grid = makeList(rows, cols)

    for r in range(rows):
        for c in range(cols):
            grid[r][c] = Cell(r, c, "neutral", randomCellType())

    # TODO: make sure it is at least rows//2 away from the opponent
    r, c = randomCoords(rows, cols)
    grid[r][c] = Cell(r, c, "player", "general")
    grid[r][c].isVisible = True

    return (grid, (r, c))


def drawBoardCells(app):
    """Draw all the cells in the board"""

    for r in range(app.board.rows):
        for c in range(app.board.cols):
            drawCell(app, app.board.at(r, c))


def hasBlockedAreas(grid):
    """Check if a generated grid has any blocked areas"""

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
    """
    Board represents the main part of the game state.
    This includes the grid, the cells, and the troops.
    It does not include the selected cell or the premoves.
    """

    def __init__(self, app, rows, cols):
        """Initialize the board"""

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
        self.grid, generalCoords = generateGrid(self.rows, self.cols)

        # regenerate grid until there are no blocked areas
        while hasBlockedAreas(self.grid):
            self.grid, generalCoords = generateGrid(self.rows, self.cols)

        app.selectedCoords = generalCoords
        app.premoveSelectedCoords = generalCoords

    def at(self, row, col):
        """
        Get the cell at a row and col, with bounds checking.
        Do not access the grid directly.
        """

        r = min(max(row, 0), self.rows - 1)
        c = min(max(col, 0), self.cols - 1)

        return self.grid[r][c]

    def step(self, mode):
        """Increment the number of troops in the cell"""

        if mode == "city":
            for row in self.grid:
                for cell in row:
                    # if is a city or general
                    if cell.t in ["city", "general"] and cell.team != "neutral":
                        cell.numTroops += 1

        if mode == "all":
            for row in self.grid:
                for cell in row:
                    cell.step()

    def collectTroops(self, coords):
        """Collect all troops into a single cell"""

        cnt = 0
        for r, row in enumerate(self.grid):
            for c, cell in enumerate(row):
                if cell.team == "player":
                    if (r, c) == coords:
                        continue
                    if cell.numTroops > 1:
                        cnt += cell.numTroops - 1
                        cell.numTroops = 1

        self.grid.at(*coords).numTroops += cnt


def drawBoard(app):
    """Draw the board"""

    drawBoardCells(app)
    drawBoardBorder(app)
