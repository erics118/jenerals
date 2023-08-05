from cmu_graphics import *

from utils.colors import Colors
from utils.tuple import add, subtract


def getPremoveCoords(app, coords):
    """Get the top left coordinate of the cell"""

    cellLeft = app.board.left + (coords[0] + 0.5) * app.cellSize
    cellTop = app.board.top + (coords[1] + 0.5) * app.cellSize

    return (cellTop, cellLeft)


def drawPremoves(app):
    """Draw the premoves"""

    for p in app.players:
        if p.selectedCoords is None:
            return

        prev = p.selectedCoords
        for premoveCoords, moveTroops in p.premoves:
            premoveCenter = getPremoveCoords(app, premoveCoords)
            delta = subtract(prev, premoveCoords)

            shift = (0, 0)
            h = app.cellSize // 2
            label = ""
            if delta == (1, 0):
                label = "↑"
                shift = (0, h)
            elif delta == (0, 1):
                label = "←"
                shift = (h, 0)
            elif delta == (-1, 0):
                label = "↓"
                shift = (0, -h)
            elif delta == (0, -1):
                label = "→"
                shift = (-h, 0)

            drawLabel(
                label,
                *add(premoveCenter, shift),
                fill=Colors.WHITE if moveTroops else Colors.RED,
                size=10,
                bold=True,
                font="symbols",
            )
            prev = premoveCoords
