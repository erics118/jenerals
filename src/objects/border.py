from cmu_graphics import *

import utils.colors as colors

# TODO: draw borders only between visible cells


def drawBoardBorder(app):
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
