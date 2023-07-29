from utils.floodFill import floodFill
from .border import drawBoardBorder
from .cell import Cell, drawCell
from cmu_graphics import *
import random


def randomCellType():
    """Generate a random cell type, with hardcoded probabilities"""

    r = random.randint(0, 99)
    if r < 15:
        return "mountain"
    elif r < 20:
        return "city"
    else:
        return "fog"


def randomCoords(rows, cols):
    """Generate a random coordinate"""

    return (random.randint(0, rows - 1), random.randint(0, cols - 1))


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

    def collectTroops(self, coords):
        """Collect all troops into a single cell"""

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
    """Draw the board"""

    drawBoardCells(app)
    drawBoardBorder(app)
