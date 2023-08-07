from cmu_graphics import *

from objects.premoves import drawPremoves
from objects.turnCounter import drawTurnCounter


def drawGame(app):
    """Draw the game"""

    app.board.draw()
    drawPremoves(app)
    drawTurnCounter(app)
    if app.ended:
        drawEndPopup(app)


def drawEndPopup(app):
    """Draw the end popup"""

    drawRect(280, 280, 240, 290, fill="white")
    drawLabel(
        f"Winner: {app.players[app.winnerId].name}!",
        400,
        340,
        fill="black",
        bold=True,
        size=18,
    )
