from cmu_graphics import *

from utils.addTuple import add

""


def getPremoveCoords(app, coords):
    """Get the top left coordinate of the cell"""

    cellLeft = app.board.left + (coords[0] + 0.5) * app.board.cellWidth
    cellTop = app.board.top + (coords[1] + 0.5) * app.board.cellHeight

    return (cellTop, cellLeft)


def drawPremoves(app):
    """Draw the premoves"""
    if app.selectedCoords == None:
        return

    currPremoveCoords = app.selectedCoords
    for premove in app.premoves:
        print(currPremoveCoords)
        print()
        drawLabel(
            "x", *getPremoveCoords(app, currPremoveCoords), fill="red", size=20
        )
        currPremoveCoords = add(currPremoveCoords, premove)
