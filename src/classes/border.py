from cmu_graphics import *

import utils.colors as colors


# TODO: draw borders only between visible cells
# Code modified from tetris grid assignment on CS Academy
def drawBoardBorder(app):
    """Draw the board border"""

    # draw the board outline with double-thickness
    drawRect(
        app.board.left,
        app.board.top,
        app.board.width,
        app.board.height,
        fill=None,
        border=colors.BORDER,
        borderWidth=2 * app.cellBorderWidth,
    )
