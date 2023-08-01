from cmu_graphics import *

from objects.accentedLabel import drawAccentedLabel
from utils.colors import Colors


def drawStartScreen(app):
    """Draw the start screen"""

    drawAccentedLabel("jenerals.io", app.width // 2, 150, size=64, bold=True)

    desc = "Protect your general. Capture enemy generals."
    drawLabel(desc, app.width // 2, 210, size=18, fill=Colors.WHITE, bold=True)

    hint = "Press 'enter' to start the game."
    drawLabel(hint, app.width // 2, 260, size=18, fill=Colors.WHITE, bold=True)
