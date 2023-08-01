from cmu_graphics import *

from utils.colors import Colors


def drawBackground(app):
    """Draw the background"""

    drawRect(0, 0, app.width, app.height, fill=Colors.BACKGROUND)
