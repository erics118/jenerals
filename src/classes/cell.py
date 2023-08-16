from dataclasses import dataclass
from cmu_graphics import *

from utils.colors import Colors
from utils.image import getImage


@dataclass
class Cell:
    """
    A single cell on the board.
    It includes the position, the team, type, the number of troops, and if the
    cell is visible. The row and col fields are only used internally, and should
    not be modified.
    """

    row: int
    col: int
    team: int
    t: str
    numTroops: int = 0
    isVisible: bool = False
    _app: any = None

    def setup(self, app):
        """Setup the cell"""
        self._app = app

    def step(self):
        """Increment the number of troops in the cell"""
        if self.team == -1:
            return

        self.numTroops += 1

    def getCellLeftTop(self):
        """Get the top left coordinate of the cell"""

        cellLeft = self._app.board.left + self.col * self._app.cellSize
        cellTop = self._app.board.top + self.row * self._app.cellSize
        return (cellLeft, cellTop)

    def getColor(self):
        """Get the color of the cell to be used when drawing"""
        isVisible = self.isVisible or self._app.forceIsVisible

        if isVisible:
            if self.team == 0:
                return Colors.BLUE
            if self.team == 1:
                return Colors.RED
            if self.t == "city":
                return Colors.VISIBLE_CITY
            if self.t == "mountain":
                return Colors.VISIBLE_MOUNTAIN

            return Colors.VISIBLE_CELL

        return Colors.FOG

    def draw(self):
        """Draw a single cell."""

        isVisible = self.isVisible or self._app.forceIsVisible

        cellLeft, cellTop = self.getCellLeftTop()
        border = None

        if isVisible:
            border = Colors.BORDER

        p = app.players[app.identity]

        if p.premoveSelectedCoords == (self.row, self.col):
            border = Colors.WHITE

        color = self.getColor()

        # is above, below, left, or right of app.selectedCoords
        if p.isFocused and p.premoveSelectedCoords in [
            (self.row - 1, self.col),
            (self.row + 1, self.col),
            (self.row, self.col - 1),
            (self.row, self.col + 1),
        ]:
            if self.team == 0:
                color = (
                    Colors.SURROUNDING_BLUE_VISIBLE
                    if isVisible
                    else Colors.SURROUNDING_FOG_NOT_VISIBLE
                )
            elif self.team == 1:
                color = (
                    Colors.SURROUNDING_RED_VISIBLE
                    if isVisible
                    else Colors.SURROUNDING_FOG_NOT_VISIBLE
                )
            else:
                if self.t == "city":
                    color = (
                        Colors.SURROUNDING_CITY_VISIBLE
                        if isVisible
                        else Colors.SURROUNDING_OBSTACLE_NOT_VISIBLE
                    )
                elif self.t == "mountain":
                    color = (
                        Colors.SURROUNDING_MOUNTAIN_VISIBLE
                        if isVisible
                        else Colors.SURROUNDING_OBSTACLE_NOT_VISIBLE
                    )
                else:
                    color = (
                        Colors.SURROUNDING_FOG_VISIBLE
                        if isVisible
                        else Colors.SURROUNDING_FOG_NOT_VISIBLE
                    )

        # draw the background for the cell
        drawRect(
            cellLeft,
            cellTop,
            self._app.cellSize,
            self._app.cellSize,
            fill=color,
            border=border,
            borderWidth=self._app.cellBorderWidth,
        )

        # draw the image for the cell if it is not fog
        image = getImage(app, self.t, isVisible)

        if image is not None:
            drawImage(
                image,
                cellLeft + self._app.cellSize // 2,
                cellTop + self._app.cellSize // 2,
                align="center",
            )

        # draw the troop count
        if isVisible and self.numTroops != 0:
            drawLabel(
                str(self.numTroops),
                cellLeft + self._app.cellSize // 2,
                cellTop + self._app.cellSize // 2,
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
    row = int((y - app.board.top) / app.cellSize)
    col = int((x - app.board.left) / app.cellSize)

    return (row, col)
