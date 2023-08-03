from cmu_graphics import *

from utils.colors import Colors


def drawTurnCounter(app):
    """Draw the turn counter in the top left corner"""

    w = 75
    h = 20
    borderWidth = 3

    # create the label
    # show a `.` after the turn if it is half step

    turn = app.c // app.stepsPerSecond
    isHalf = (app.c * 2 // app.stepsPerSecond) % 2 == 1
    label = f"Turn {turn}"

    if isHalf:
        h += 0.7
        label += "."

    # draw the outer rect for accent color
    drawRect(0, 0, w + borderWidth, h + borderWidth, fill=Colors.ACCENT)

    # draw the inner rect for white
    drawRect(0, 0, w, h, fill=Colors.WHITE)

    drawLabel(label, 10, 10, size=14, fill=Colors.BLACK, align="left")
