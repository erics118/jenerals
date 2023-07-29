from objects.board import drawBoard
from cmu_graphics import *
import utils.colors as colors


def drawBackground(app):
    """Draw the background"""

    drawRect(0, 0, app.width, app.height, fill=colors.BACKGROUND)


def drawTurnCounter(app):
    """Draw the turn counter in the top left corner"""

    w = 75
    h = 20
    borderWidth = 3

    # draw the outer rect for accent color
    drawRect(0, 0, w + borderWidth, h + borderWidth, fill=colors.ACCENT)

    # draw the inner rect for white
    drawRect(0, 0, w, h, fill=colors.WHITE)

    # create the label
    # show a `.` after the turn if it is
    label = f"Turn {app.c//2}"
    if app.c % 2 == 1:
        label += "."

    drawLabel(label, w // 2, h // 2, size=14, fill=colors.BLACK, align="center")


def drawAccentedLabel(label, x, y, **kwargs):
    """Draw a label with a box, and an accented shadow"""

    drawLabel(label, x + 3, y + 3, **kwargs, fill=colors.ACCENT)
    drawLabel(label, x, y, **kwargs, fill=colors.WHITE)


def drawStartScreen(app):
    """Draw the start screen"""

    drawAccentedLabel("jenerals.io", app.width // 2, 150, size=64, bold=True)

    desc = "Protect your jeneral. Capture enemy jenerals."
    drawLabel(desc, app.width // 2, 200, size=18, fill=colors.WHITE, bold=True)


def drawGame(app):
    drawBoard(app)
    drawTurnCounter(app)


def drawAll(app):
    drawBackground(app)

    if not app.hasOngoingGame:
        drawStartScreen(app)
    else:
        drawGame(app)

    if app.flag:
        drawRect(10, 10, 30, 30, fill="red")
