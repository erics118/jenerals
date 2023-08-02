from cmu_graphics import *
from PIL import Image

from utils.colors import Colors
from utils.image import getImagePath


class Cell:
    """
    A single cell on the board.
    It includes the position, the team, type, the number of troops, and if the cell is visible.

    The row and col fields are sometimes redundant if the cell is in a Board.
    Nevertheless, they are useful in other cases.
    """

    def __init__(self, app, row, col, team, t, numTroops=0, isVisible=False):
        """Initialize the cell"""
        self.app = app

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

    def getCellLeftTop(self):
        """Get the top left coordinate of the cell"""

        cellLeft = self.app.board.left + self.col * self.app.board.cellSize
        cellTop = self.app.board.top + self.row * self.app.board.cellSize
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

    # TODO: some borders are missing when having premoves
    def draw(self):
        isVisible = self.isVisible or self.app.forceIsVisible
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
            if (
                app.board.at((self.row + drow, self.col + dcol)).team
                == "player"
            ):
                app.board.at((self.row, self.col)).isVisible = True

        cellLeft, cellTop = self.getCellLeftTop()
        border = None

        if isVisible:
            border = Colors.BORDER
        if self.app.premoveSelectedCoords == (self.row, self.col):
            border = Colors.WHITE

        color = self.getColor(self.app.forceIsVisible)

        # is above, below, left, or right of app.selectedCoords
        if self.app.isFocused and self.app.premoveSelectedCoords in [
            (self.row - 1, self.col),
            (self.row + 1, self.col),
            (self.row, self.col - 1),
            (self.row, self.col + 1),
        ]:
            # TODO: diff colors depending on existing color
            if self.t == "fog" or self.t == "mountain" or self.t == "city":
                if self.team == "player":
                    # must be visible?
                    color = Colors.SURROUNDING_BLUE_VISIBLE
                else:
                    if self.t == "city":
                        if isVisible:
                            color = Colors.SURROUNDING_CITY_VISIBLE
                        else:
                            color = Colors.SURROUNDING_OBSTACLE_NOT_VISIBLE
                    elif self.t == "mountain":
                        if isVisible:
                            color = Colors.SURROUNDING_MOUNTAIN_VISIBLE
                        else:
                            color = Colors.SURROUNDING_OBSTACLE_NOT_VISIBLE
                    else:
                        if isVisible:
                            color = Colors.SURROUNDING_FOG_VISIBLE
                        else:
                            color = Colors.SURROUNDING_FOG_NOT_VISIBLE

        # draw the background for the cell
        drawRect(
            cellLeft,
            cellTop,
            self.app.board.cellSize,
            self.app.board.cellSize,
            fill=color,
            border=border,
            borderWidth=self.app.cellBorderWidth,
        )

        # draw the image for the cell if it is not fog
        imagePath = getImagePath(
            self.t, self.isVisible or self.app.forceIsVisible
        )

        if imagePath is not None:
            # get the PIL image
            image = Image.open(imagePath)

            # resize the image
            image.thumbnail(
                (app.board.cellSize * 0.8, app.board.cellSize * 0.8)
            )

            # draw the image
            drawImage(
                CMUImage(image),
                cellLeft + self.app.board.cellSize // 2,
                cellTop + self.app.board.cellSize // 2,
                align="center",
            )

        # draw the troop count
        if (
            self.t == "general"
            or (self.t == "city" and isVisible)
            or (self.numTroops != 0 and self.t == "fog")
        ):
            drawLabel(
                str(self.numTroops),
                cellLeft + self.app.board.cellSize // 2,
                cellTop + self.app.board.cellSize // 2,
                size=13,
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
    row = int((y - app.board.top) / app.board.cellSize)
    col = int((x - app.board.left) / app.board.cellSize)

    return (row, col)
