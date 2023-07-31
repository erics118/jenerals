from cmu_graphics import *

from classes.board import drawBoard
from utils.colors import Colors


def drawBackground(app):
    """Draw the background"""

    drawRect(0, 0, app.width, app.height, fill=Colors.BACKGROUND)


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


def drawAccentedLabel(label, x, y, **kwargs):
    """Draw a label with a box, and an accented shadow"""

    drawLabel(label, x + 3, y + 3, **kwargs, fill=Colors.ACCENT)
    drawLabel(label, x, y, **kwargs, fill=Colors.WHITE)


def drawStartScreen(app):
    """Draw the start screen"""

    drawAccentedLabel("jenerals.io", app.width // 2, 150, size=64, bold=True)

    desc = "Protect your general. Capture enemy generals."
    drawLabel(desc, app.width // 2, 200, size=18, fill=Colors.WHITE, bold=True)

    hint = "Press 'enter' to start the game."
    drawLabel(hint, app.width // 2, 250, size=18, fill=Colors.WHITE, bold=True)


def drawGame(app):
    """Draw the game"""

    drawBoard(app)
    drawTurnCounter(app)


def drawAll(app):
    """Draw all elements of the app"""

    drawBackground(app)

    if not app.hasOngoingGame:
        drawStartScreen(app)
    else:
        drawGame(app)

    if app.flag:
        drawRect(10, 10, 30, 30, fill="red")

    for button in app.buttons:
        button.draw()
