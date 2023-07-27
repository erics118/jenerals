
from cmu_graphics import *

import utils.colors as colors

def drawBoardBorder(app):
    # draw the board outline (with double-thickness):
    drawRect(
        app.boardLeft,
        app.boardTop,
        app.boardWidth,
        app.boardHeight,
        fill=None,
        border=colors.BORDER,
        borderWidth=2 * app.cellBorderWidth,
    )
