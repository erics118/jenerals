import utils.colors as colors
from cmu_graphics import *


class Cell:
    def __init__(self, row, col, team, t, numTroops=0, isVisible=False):
        self.row = row
        self.col = col
        self.team = team  # player, bot, neutral
        self.t = t  # obstacle, city, mountain, general, fog
        self.numTroops = numTroops
        self.isVisible = isVisible

    def step(self):
        if self.numTroops > 0:
            self.numTroops += 1

    def isSelectable(self):
        self.team == "red"

    def getCellLeftTop(self, app):
        cellLeft = app.board.left + self.col * app.board.cellWidth
        cellTop = app.board.top + self.row * app.board.cellHeight
        return (cellLeft, cellTop)

    def getColor(self, forceIsVisible=False):
        if self.team == "player":
            return colors.BLUE

        if self.isVisible or forceIsVisible:
            if self.team == "bot":
                return colors.RED
            elif self.t == "city":
                return colors.VISIBLE_CITY
            else:  # self.team == "neutral"
                return colors.VISIBLE_CELL

        return colors.FOG

    def getImage(self, forceIsVisible=False):
        if self.isVisible or forceIsVisible:
            return self.t
        else:
            if self.t in ["mountain", "city"]:
                return "obstacle"
        return None



def drawCell(app, cell):
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
        if app.board.at(cell.row + drow, cell.col + dcol).team == "player":
            app.board.at(cell.row, cell.col).isVisible = True

    cellLeft, cellTop = cell.getCellLeftTop(app)
    border = colors.BORDER
    color = cell.getColor()

    # if is selectedCoords

    if app.premoveSelectedCoords == (cell.row, cell.col):
        # color = colors.VISIBLE_CELL
        border = colors.WHITE
    # is above, below, left, or right of app.selectedCoords
    if app.isFocused and app.premoveSelectedCoords in [
        (cell.row - 1, cell.col),
        (cell.row + 1, cell.col),
        (cell.row, cell.col - 1),
        (cell.row, cell.col + 1),
    ]:
        # TODO: diff colors depending on existing color

        color = colors.SURROUNDING_FOCUSED_NEUTRAL

    drawRect(
        cellLeft,
        cellTop,
        app.board.cellWidth,
        app.board.cellHeight,
        fill=color,
        border=border,
        borderWidth=app.cellBorderWidth,
    )

    if cell.t != "fog":
        imagePath = cell.getImage(app.forceIsVisible)
        if imagePath is not None:
            drawImage(
                "./src/images/" + imagePath + ".png",
                cellLeft + app.board.cellHeight // 2,
                cellTop + app.board.cellHeight // 2,
                align="center",
            )

    # troop count
    if cell.numTroops > 0 or (cell.t in ["general", "city"] and cell.team != "neutral"):
        drawLabel(
            str(cell.numTroops),
            cellLeft + app.board.cellHeight // 2,
            cellTop + app.board.cellHeight // 2,
            size=14,
            fill=colors.WHITE,
            bold=False,
        )


def drawBoardCells(app):
    for row in range(app.board.rows):
        for col in range(app.board.cols):
            drawCell(app, app.board.at(row, col))


def getCellCoords(app, x, y):
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
