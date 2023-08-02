from cmu_graphics import *

from utils.addTuple import add
from utils.colors import Colors


def getPremoveCoords(app, coords):
    """Get the top left coordinate of the cell"""

    cellLeft = app.board.left + (coords[0] + 0.5) * app.board.cellSize
    cellTop = app.board.top + (coords[1] + 0.5) * app.board.cellSize

    return (cellTop, cellLeft)


def drawPremoves(app):
    """Draw the premoves"""
    if app.selectedCoords == None:
        return

    currPremoveCoords = app.selectedCoords
    for premove in app.premoves:
        shift = (0, 0)
        h = app.board.cellSize // 2

        if premove == (1, 0):
            label = "↓"
            shift = (0, h)
        elif premove == (0, 1):
            label = "→"
            shift = (h, 0)
        elif premove == (-1, 0):
            label = "↑"
            shift = (0, -h)
        elif premove == (0, -1):
            label = "←"
            shift = (-h, 0)

        premoveCoords = add(getPremoveCoords(app, currPremoveCoords), shift)
        currPremoveCoords = add(currPremoveCoords, premove)
        drawLabel(
            label,
            *premoveCoords,
            fill=Colors.WHITE,
            size=15,
            bold=True,
            font="symbols",
        )
