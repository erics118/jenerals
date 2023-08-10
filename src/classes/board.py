from dataclasses import dataclass
from random import randint

from cmu_graphics import *

from classes.cell import Cell
from utils.colors import Colors
from utils.floodFill import floodFill


def randomCellType():
    """Generate a random cell type, with hardcoded probabilities"""

    r = randint(0, 99)

    if r < 5:
        return "mountain"

    if r < 10:
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

    # randomly generate the grid
    for r in range(rows):
        for c in range(cols):
            grid[r][c] = Cell(r, c, -1, randomCellType())
            grid[r][c].setup(app)
            # random number of troops for cities
            if grid[r][c].t == "city":
                grid[r][c].numTroops = randomCityTroops()

    dist = 0

    # make sure the two generals are at least 0.3 of the board away from each other
    while dist < (rows + cols) * 0.3:
        r1, c1 = randomCoords(rows, cols)
        r2, c2 = randomCoords(rows, cols)

        dist = abs(r1 - r2) + abs(c1 - c2)

    grid[r1][c1] = Cell(r1, c1, 0, "general")
    grid[r1][c1].setup(app)
    grid[r1][c1].isVisible = app.identity == 0
    grid[r1][c1].numTroops = 1

    grid[r2][c2] = Cell(r2, c2, 1, "general")
    grid[r2][c2].setup(app)
    grid[r2][c2].isVisible = app.identity == 1
    grid[r2][c2].numTroops = 1

    return (grid, [(r1, c1), (r2, c2)])


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
            if grid[r][c].t in ["general", "fog"]:
                tempGrid[r][c] = 0
            else:
                tempGrid[r][c] = 1

    # flood fill, making visited cells 2
    floodFill(tempGrid)

    # true if there are any 0's, meaning unvisited cells
    # CITE: https://docs.python.org/3/library/functions.html#any
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
            if grid[r][c].t in ["general", "fog", "city"]:
                tempGrid[r][c] = 0
            else:
                tempGrid[r][c] = 1

    # flood fill, making visited cells 2
    floodFill(tempGrid)

    # true if there are any 0's, meaning unvisited cells
    # CITE: https://docs.python.org/3/library/functions.html#any
    return any(0 in r for r in tempGrid)


@dataclass
class Board:
    """
    Board represents the main part of the game state.
    This includes the grid, the cells, and the troops.
    It does not include the selected cell or the premoves.
    """

    grid: list = None
    rows: int = 20
    cols: int = 20
    left: int = 80
    top: int = 80
    width: int = 800
    height: int = 800
    _app: any = None

    def setup(self, app, generateNew):
        """Setup the board"""
        self._app = app

        if generateNew:
            # randomly generate the grid
            self.grid, generalCoords = generateGrid(app, self.rows, self.cols)

            # regenerate grid until there are no blocked areas
            while hasBlockedCity(self.grid) or hasBlockedFog(self.grid):
                self.grid, generalCoords = generateGrid(app, self.rows, self.cols)
        else:
            generalCoords = [None] * 2
            for row in self.grid:
                for cell in row:
                    cell.isVisible = app.identity == cell.team
                    if cell.t == "general":
                        generalCoords[cell.team] = (cell.row, cell.col)

        app.board.step("visible")

        for playerId, coords in enumerate(generalCoords):
            app.players[playerId].generalCoord = coords
            app.players[playerId].selectedCoords = coords
            app.players[playerId].premoveSelectedCoords = coords

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
                        cell = self._app.board.at((row + drow, col + dcol)).team
                        if cell == self._app.identity:
                            self._app.board.at((row, col)).isVisible = True

        elif mode == "city":
            for row in self.grid:
                for cell in row:
                    # if is a city or general
                    if cell.t in ["city", "general"]:
                        cell.step()

        elif mode == "all":
            for row in self.grid:
                for cell in row:
                    cell.step()

    def drawCells(self):
        """Draw all the cells in the board"""

        for r in range(self._app.board.rows):
            for c in range(self._app.board.cols):
                self._app.board.at((r, c)).draw()

    # CITE: code modified from tetris grid assignment on CS Academy
    def drawBorder(self):
        """Draw the board border"""

        # draw the board outline with double-thickness
        drawRect(
            self._app.board.left,
            self._app.board.top,
            640,
            640,
            fill=None,
            border=Colors.BORDER,
            borderWidth=2 * self._app.cellBorderWidth,
        )

    def draw(self):
        """Draw the board"""

        self.drawCells()
        self.drawBorder()
