import utils.colors as colors
from cmu_graphics import *


class Cell:
    def __init__(self, row, col, color, image):
        self.row = row
        self.col = col
        self.color = color if color != None else colors.FOG
        self.image = image

    def getCellLeftTop(self, app):
        cellLeft = app.boardLeft + self.col * app.cellWidth
        cellTop = app.boardTop + self.row * app.cellHeight
        return (cellLeft, cellTop)


def drawCell(app, cell):
    cellLeft, cellTop = cell.getCellLeftTop(app)
    drawRect(
        cellLeft,
        cellTop,
        app.cellWidth,
        app.cellHeight,
        fill=cell.color,
        border=None,
        borderWidth=app.cellBorderWidth,
    )

    if cell.image != None:
        imagePath = "./src/images/" + cell.image + ".png"
        drawImage(imagePath, cellLeft + 2, cellTop + 2)


def drawBoardCells(app):
    drawRect(0, 0, app.width, app.height, fill=colors.BACKGROUND)

    for row in range(app.rows):
        for col in range(app.cols):
            cell = Cell(row, col, None, None)
            if app.board[row][col] == "city":
                cell.color = colors.FOG
                cell.image = "city"
            elif app.board[row][col] == "general1":
                cell.color = colors.BLUE
                cell.image = "crown"
            elif app.board[row][col] == "general2":
                cell.color = colors.RED
                cell.image = "crown"
            elif app.board[row][col] == "mountain":
                cell.color = colors.FOG
                cell.image = "mountain"
            elif app.board[row][col] == "obstacle":
                cell.color = colors.FOG
                cell.image = "obstacle"
            drawCell(app, cell)
