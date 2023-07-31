from utils.colors import Colors
from cmu_graphics import *

from utils.image import getImagePath


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

        if self.numTroops > 0:
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


def drawCell(app, cell):
    """Draw a single cell."""

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

    # TODO: move to board class so not called too repetitively
    for drow, dcol in directions:
        if app.board.at((cell.row + drow, cell.col + dcol)).team == "player":
            app.board.at((cell.row, cell.col)).isVisible = True

    cellLeft, cellTop = cell.getCellLeftTop(app)
    border = Colors.BORDER
    color = cell.getColor()

    # if is selectedCoords

    if app.premoveSelectedCoords == (cell.row, cell.col):
        # color = Colors.VISIBLE_CELL
        border = Colors.WHITE
    # is above, below, left, or right of app.selectedCoords
    if app.isFocused and app.premoveSelectedCoords in [
        (cell.row - 1, cell.col),
        (cell.row + 1, cell.col),
        (cell.row, cell.col - 1),
        (cell.row, cell.col + 1),
    ]:
        # TODO: diff colors depending on existing color
        if cell.t == "fog" or cell.t == "mountain" or cell.t == "city":
            if cell.team == "player":
                # must be visible?
                color = Colors.SURROUNDING_BLUE_VISIBLE
            else:
                if cell.t == "mountain" or cell.t == "city":
                    color = Colors.SURROUNDING_OBSTACLE_VISIBLE
                else:
                    if cell.isVisible:
                        color = Colors.SURROUNDING_FOG_VISIBLE
                    else:
                        color = Colors.SURROUNDING_FOG_NOT_VISIBLE

    # draw the background for the cell
    drawRect(
        cellLeft,
        cellTop,
        app.board.cellWidth,
        app.board.cellHeight,
        fill=color,
        border=border,
        borderWidth=app.cellBorderWidth,
    )

    # draw the image for the cell if it is not fog
    imagePath = getImagePath(cell.t, cell.isVisible or app.forceIsVisible)

    if imagePath is not None:
        drawImage(
            imagePath,
            cellLeft + app.board.cellHeight // 2,
            cellTop + app.board.cellHeight // 2,
            align="center",
        )

    # draw the troop count
    if cell.numTroops > 0 or (
        cell.t in ["general", "city"] and cell.team != "neutral"
    ):
        drawLabel(
            str(cell.numTroops),
            cellLeft + app.board.cellHeight // 2,
            cellTop + app.board.cellHeight // 2,
            size=12,
            fill=Colors.WHITE,
            bold=False,
        )


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
