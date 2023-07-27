import utils.colors as colors
from cmu_graphics import *


class Cell:
    def __init__(self, row, col, team, t, numTroops, isVisible=True):
        self.row = row
        self.col = col
        self.team = team  # player, bot, neutral
        self.t = t  # obstacle, city, mountain, general, fog
        self.numTroops = numTroops
        self.isVisible = isVisible

    def step(self):
        self.numTroops += 1

    def isSelectable(self):
        self.team == "red"

    def getCellLeftTop(self, app):
        cellLeft = app.boardLeft + self.col * app.cellWidth
        cellTop = app.boardTop + self.row * app.cellHeight
        return (cellLeft, cellTop)

    def getColor(self):
        if self.team == "player":
            return colors.BLUE
        elif self.team == "neutral":
            return colors.VISIBLE_CELL

        if self.isVisible:
            if self.team == "bot":
                return colors.RED
            elif self.team == "neutral":
                return colors.VISIBLE_CELL
        else:
            return colors.FOG


def drawCell(app, cell):
    cellLeft, cellTop = cell.getCellLeftTop(app)
    border = colors.BORDER
    color = cell.getColor()

    # if is selectedCell
    if app.isFocused:
        if app.selectedCell == (cell.row, cell.col):
            color = colors.VISIBLE_CELL
            border = colors.WHITE
        # is above, below, left, or right of app.selectedCell
        elif app.selectedCell in [
            (cell.row - 1, cell.col),
            (cell.row + 1, cell.col),
            (cell.row, cell.col - 1),
            (cell.row, cell.col + 1),
        ]:
            # todo: diff colors depending on existing color
            color = rgb(108, 108, 108)

    drawRect(
        cellLeft,
        cellTop,
        app.cellWidth,
        app.cellHeight,
        fill=color,
        border=border,
        borderWidth=app.cellBorderWidth,
    )

    if cell.t != "fog":
        imageName = ""
        if cell.t == "city":
            imageName = "city"
        elif cell.t == "mountain":
            imageName = "mountain"
        elif cell.t == "obstacle":
            imageName = "obstacle"
        elif cell.t == "general":
            imageName = "crown"
        else:
            print("wtf")

        imagePath = "./src/images/" + imageName + ".png"
        drawImage(
            imagePath,
            cellLeft + app.cellHeight // 2,
            cellTop + app.cellHeight // 2,
            align="center",
        )

    # troop count
    if cell.numTroops > 0:
        drawLabel(
            str(cell.numTroops),
            cellLeft + app.cellHeight // 2,
            cellTop + app.cellHeight // 2,
            size=14,
            fill=colors.WHITE,
            bold=True
        )


def drawBoardCells(app):
    drawRect(0, 0, app.width, app.height, fill=colors.BACKGROUND)

    for row in range(app.rows):
        for col in range(app.cols):
            # cell = Cell(row, col, "player", "fog", 1)
            # if app.board[row][col] == "city":
            #     cell.color = colors.FOG
            #     cell.image = "city"
            # elif app.board[row][col] == "general":
            #     cell.color = colors.BLUE
            #     cell.image = "crown"
            # elif app.board[row][col] == "general2":
            #     cell.color = colors.RED
            #     cell.image = "crown"
            # elif app.board[row][col] == "mountain":
            #     cell.color = colors.FOG
            #     cell.image = "mountain"
            # elif app.board[row][col] == "obstacle":
            #     cell.color = colors.FOG
            #     cell.image = "obstacle"

            drawCell(app, app.board[row][col])


def getCell(app, x, y):
    # out of bounds of board
    if (
        x < app.boardLeft
        or x > app.boardLeft + app.boardWidth
        or y < app.boardTop
        or y > app.boardTop + app.boardHeight
    ):
        return None
    row = int((y - app.boardTop) / app.cellHeight)
    col = int((x - app.boardLeft) / app.cellWidth)
    return (row, col)
