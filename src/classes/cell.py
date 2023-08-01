from cmu_graphics import *

from utils.colors import Colors


class Cell:
    """
    A single cell on the board.
    It includes the position, the team, type, the number of troops, and if the cell is visible.

    The row and col fields are sometimes redundant if the cell is in a Board.
    Nevertheless, they are useful in other cases.
    """

    def __init__(self, row, col, team, t, numTroops=0, isVisible=False):
        """Initialize the cell"""

        self.row = row
        self.col = col
        self.team = team  # player, bot, neutral
        self.t = t  # obstacle, city, mountain, general, fog
        self.numTroops = numTroops
        self.isVisible = isVisible

    def step(self):
        """Increment the number of troops in the cell"""

        if self.t == "city" and self.team == "neutral":
            return

        if self.numTroops != 0:
            self.numTroops += 1

    # TODO: implement this
    def isSelectable(self):
        """
        Return whether the cell is selectable.
        A cell is not selectable if it is a city or general, but selectable otherwise.
        """

    def getCellLeftTop(self, app):
        """Get the top left coordinate of the cell"""

        cellLeft = app.board.left + self.col * app.board.cellWidth
        cellTop = app.board.top + self.row * app.board.cellHeight
        return (cellLeft, cellTop)

    def getColor(self, forceIsVisible=False):
        """Get the color of the cell to be used when drawing"""

        if self.team == "player":
            return Colors.BLUE

        if self.isVisible or forceIsVisible:
            if self.team == "bot":
                return Colors.RED
            elif self.t == "city":
                return Colors.VISIBLE_CITY
            elif self.t == "mountain":
                return Colors.VISIBLE_MOUNTAIN
            else:  # self.team == "neutral"
                return Colors.VISIBLE_CELL

        return Colors.FOG


# CITE: code modified from tetris grid assignment on CS Academy
def getCellCoords(app, x, y):
    """
    Given x and y coordinates, get the row and col
    of the cell that contains those coordinates
    """

    # out of bounds of board
    if (
        x < app.board.left
        or x > app.board.left + app.board.width
        or y < app.board.top
        or y > app.board.top + app.board.height
    ):
        return None
    row = int((y - app.board.top) / app.board.cellHeight)
    col = int((x - app.board.left) / app.board.cellWidth)

    return (row, col)
