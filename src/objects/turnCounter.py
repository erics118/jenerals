from cmu_graphics import *

from utils.colors import Colors


def drawTurnCounter(app):
    """Draw the turn counter in the top left corner"""

    w = 75
    h = 20
    borderWidth = 3

    # draw the outer rect for accent color
    drawRect(0, 0, w + borderWidth, h + borderWidth, fill=Colors.ACCENT)

    # draw the inner rect for white
    drawRect(0, 0, w, h, fill=Colors.WHITE)

    # create the label
    # show a `.` after the turn if it is
    label = f"Turn {app.c//2}"
    if app.c % 2 == 1:
        label += "."

    drawLabel(label, w // 2, h // 2, size=14, fill=Colors.BLACK, align="center")
