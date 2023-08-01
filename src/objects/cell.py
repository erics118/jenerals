from cmu_graphics import *

from utils.colors import Colors
from utils.image import getImagePath


def drawCell(app, cell):
    isVisible = cell.isVisible or app.forceIsVisible
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
    border = None

    if isVisible:
        border = Colors.BORDER
    if app.premoveSelectedCoords == (cell.row, cell.col):
        border = Colors.WHITE

    color = cell.getColor(app.forceIsVisible)

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
                if cell.t == "city":
                    if isVisible:
                        color = Colors.SURROUNDING_CITY_VISIBLE
                    else:
                        color = Colors.SURROUNDING_OBSTACLE_NOT_VISIBLE
                elif cell.t == "mountain":
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
    if (
        cell.t == "general"
        or (cell.t == "city" and isVisible)
        or (cell.numTroops != 0 and cell.t == "fog")
    ):
        drawLabel(
            str(cell.numTroops),
            cellLeft + app.board.cellHeight // 2,
            cellTop + app.board.cellHeight // 2,
            size=13,
            fill=Colors.WHITE,
            bold=False,
        )
