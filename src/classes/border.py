from cmu_graphics import *

from utils.colors import Colors


# TODO: draw borders only between visible cells
# CITE: code modified from tetris grid assignment on CS Academy
def drawBoardBorder(app):
    """Draw the board border"""

    # draw the board outline with double-thickness
    drawRect(
        app.board.left,
        app.board.top,
        app.board.width,
        app.board.height,
        fill=None,
        border=Colors.BORDER,
        borderWidth=2 * app.cellBorderWidth,
    )
