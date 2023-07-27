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

    def getColor(self):
        if self.team == "player":
            return colors.BLUE

        if self.isVisible and self.team == "bot":
            return colors.RED

        return colors.FOG

    def getImage(self):
        if self.isVisible:
            return self.t
        else:
            if self.t in ["mountain", "city"]:
                return "obstacle"
            else:
                return "fog"


def drawCell(app, cell):
    cellLeft, cellTop = cell.getCellLeftTop(app)
    border = colors.BORDER
    color = cell.getColor()

    # if is selectedCoords
    if app.isFocused:
        if app.selectedCoords == (cell.row, cell.col):
            color = colors.VISIBLE_CELL
            border = colors.WHITE
        # is above, below, left, or right of app.selectedCoords
        elif app.selectedCoords in [
            (cell.row - 1, cell.col),
            (cell.row + 1, cell.col),
            (cell.row, cell.col - 1),
            (cell.row, cell.col + 1),
        ]:
            # TODO: diff colors depending on existing color
            color = rgb(108, 108, 108)

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
        imagePath = "./src/images/" + cell.t + ".png"
        drawImage(
            imagePath,
            cellLeft + app.board.cellHeight // 2,
            cellTop + app.board.cellHeight // 2,
            align="center",
        )

    # troop count
    if cell.numTroops > 0:
        drawLabel(
            str(cell.numTroops),
            cellLeft + app.board.cellHeight // 2,
            cellTop + app.board.cellHeight // 2,
            size=14,
            fill=colors.WHITE,
            bold=True,
        )


def drawBoardCells(app):
    drawRect(0, 0, app.width, app.height, fill=colors.BACKGROUND)

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
