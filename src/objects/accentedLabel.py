from cmu_graphics import *

from utils.colors import Colors


def drawAccentedLabel(label, x, y, **kwargs):
    """Draw a label with a box, and an accented shadow"""

    drawLabel(label, x + 3, y + 3, **kwargs, fill=Colors.ACCENT)
    drawLabel(label, x, y, **kwargs, fill=Colors.WHITE)
