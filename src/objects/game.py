from cmu_graphics import *

from objects.premoves import drawPremoves
from objects.turnCounter import drawTurnCounter
from objects.leaderboard import drawLeaderboard


def drawGame(app):
    """Draw the game"""

    app.board.draw()
    drawPremoves(app)
    drawTurnCounter(app)
    drawLeaderboard(app)
    if app.ended:
        drawEndPopup(app)


def drawEndPopup(app):
    """Draw the end popup"""

    drawRect(280, 280, 240, 290, fill="white")
    drawLabel(
        "You won!" if app.winnerId == app.identity else "You lost!",
        400,
        330,
        fill="black",
        bold=True,
        size=18,
    )
    drawLabel(
        f"Winner: {app.players[app.winnerId].name}!",
        400,
        350,
        fill="black",
        bold=True,
        size=18,
    )
