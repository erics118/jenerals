from random import randint

from cmu_graphics import *

from classes.cell import Cell
from utils.colors import Colors
from utils.floodFill import floodFill


def randomCellType():
    """Generate a random cell type, with hardcoded probabilities"""

    r = randint(0, 99)

    if r < 23:
        return "mountain"

    if r < 26:
        return "city"

    return "fog"


def randomCityTroops():
    """Generate a random number of troops for the city"""
    return randint(40, 50)


def randomCoords(rows, cols):
    """Generate a random coordinate"""

    return (randint(0, rows - 1), randint(0, cols - 1))


def generateGrid(app, rows, cols):
    """
    Generate a random grid

    Returns the grid and the coordinates of the general
    The general is the starting selected cell
    """

    grid = makeList(rows, cols)

    for r in range(rows):
        for c in range(cols):
            grid[r][c] = Cell(app, r, c, "neutral", randomCellType())
            if grid[r][c].t == "city":
                grid[r][c].numTroops = randomCityTroops()

    # TODO: make sure it is at least rows//2 away from the opponent
    r, c = randomCoords(rows, cols)
    grid[r][c] = Cell(app, r, c, "player", "general")
    grid[r][c].isVisible = True

    return (grid, (r, c))


def hasBlockedFog(grid):
    """Check if a generated grid has any blocked areas"""

    rows = len(grid)
    cols = len(grid[0])

    # 0 is unvisited
    # 1 is blocked
    # 2 is visited
    tempGrid = makeList(rows, cols)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c].t == "general" or grid[r][c].t == "fog":
                tempGrid[r][c] = 0
            else:
                tempGrid[r][c] = 1

    # flood fill, making visited cells 2
    floodFill(tempGrid)

    # true if there are any 0's, meaning unvisited cells
    return any(0 in r for r in tempGrid)


def hasBlockedCity(grid):
    """Check if a generated grid has any blocked areas"""

    rows = len(grid)
    cols = len(grid[0])

    # 0 is unvisited
    # 1 is blocked
    # 2 is visited
    tempGrid = makeList(rows, cols)

    for r in range(rows):
        for c in range(cols):
            if (
                grid[r][c].t == "general"
                or grid[r][c].t == "fog"
                or grid[r][c].t == "city"
            ):
                tempGrid[r][c] = 0
            else:
                tempGrid[r][c] = 1

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

        self.app = app

        # static board properties
        self.rows = rows
        self.cols = cols

        self.left = 80
        self.top = 80

        self.width = self.cols * app.cellSize
        self.height = self.rows * app.cellSize

        # randomly generate the grid
        self.grid, generalCoords = generateGrid(app, self.rows, self.cols)

        # regenerate grid until there are no blocked areas
        while hasBlockedCity(self.grid) or hasBlockedFog(self.grid):
            self.grid, generalCoords = generateGrid(app, self.rows, self.cols)

        app.selectedCoords = generalCoords
        app.premoveSelectedCoords = generalCoords

    def at(self, coords):
        """
        Get the cell at a row and col, with bounds checking.
        Do not access the grid directly.
        """

        r = min(max(coords[0], 0), self.rows - 1)
        c = min(max(coords[1], 0), self.cols - 1)

        return self.grid[r][c]

    def step(self, mode):
        """Increment the number of troops in the cell"""

        directions = [
            (-1, +1),
            (0, +1),
            (+1, +1),
            (-1, 0),
            (+1, 0),
            (-1, -1),
            (0, -1),
            (+1, -1),
        ]
        if mode == "visible":
            # update visibility for every cell
            for row in range(len(self.grid)):
                for col in range(len(self.grid[0])):
                    for drow, dcol in directions:
                        if (
                            app.board.at((row + drow, col + dcol)).team
                            == "player"
                        ):
                            app.board.at((row, col)).isVisible = True

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

        self.at(coords).numTroops += cnt

    def drawCells(self):
        """Draw all the cells in the board"""

        for r in range(self.app.board.rows):
            for c in range(self.app.board.cols):
                self.app.board.at((r, c)).draw()

    # CITE: code modified from tetris grid assignment on CS Academy
    def drawBorder(self):
        """Draw the board border"""

        # draw the board outline with double-thickness
        drawRect(
            self.app.board.left,
            self.app.board.top,
            self.app.board.width,
            self.app.board.height,
            fill=None,
            border=Colors.BORDER,
            borderWidth=2 * self.app.cellBorderWidth,
        )

    def draw(self):
        """Draw the board"""

        self.drawCells()
        self.drawBorder()
