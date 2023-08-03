from cmu_graphics import *

from utils.colors import Colors


def getPremoveCoords(app, coords):
    """Get the top left coordinate of the cell"""

    cellLeft = app.board.left + (coords[0] + 0.5) * app.cellSize
    cellTop = app.board.top + (coords[1] + 0.5) * app.cellSize

    return (cellTop, cellLeft)


def drawPremoves(app):
    """Draw the premoves"""
    if app.selectedCoords == None:
        return

    currPremoveCoords = app.selectedCoords
    for premoveCoords in app.premoves:
        # shift = (0, 0)
        # h = app.cellSize // 2
        label = "x"
        # if premove == (1, 0):
        #     label = "↓"
        #     shift = (0, h)
        # elif premove == (0, 1):
        #     label = "→"
        #     shift = (h, 0)
        # elif premove == (-1, 0):
        #     label = "↑"
        #     shift = (0, -h)
        # elif premove == (0, -1):
        #     label = "←"
        #     shift = (-h, 0)

        # premoveCoords = add(getPremoveCoords(app, currPremoveCoords), shift)
        # currPremoveCoords = add(currPremoveCoords, premove)

        a = getPremoveCoords(app, premoveCoords)
        drawLabel(
            label, *a, fill=Colors.RED, size=10, bold=True, font="symbols"
        )
