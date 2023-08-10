from cmu_graphics import *


def drawLeaderboard(app):
    """Draws the leaderboard on the right side of the screen."""

    # draw leaderboard
    rowHeight = 34
    playerColWidth = 82
    armyColWidth = 54
    landColWidth = 50

    numPlayers = len(app.players)

    # background
    drawRect(
        app.width - landColWidth - armyColWidth - playerColWidth,
        0,
        playerColWidth + armyColWidth + landColWidth,
        (numPlayers + 1) * rowHeight,
        fill="white",
    )

    # player heading
    drawLabel(
        "Player",
        app.width - landColWidth - armyColWidth - playerColWidth / 2,
        rowHeight / 2,
        fill="black",
        align="center",
        size=14,
    )

    drawLabel(
        "Army",
        app.width - landColWidth - armyColWidth / 2,
        rowHeight / 2,
        fill="black",
        align="center",
        size=14,
    )

    drawLabel(
        "Land",
        app.width - landColWidth / 2,
        rowHeight / 2,
        fill="black",
        align="center",
        size=14,
    )

    # sort just player ids based on troop count
    sortedPlayers = sorted(
        list(range(len(app.players))),
        key=lambda playerId: app.board.countTroops(playerId),
        reverse=True,
    )

    for i, playerId in enumerate(sortedPlayers):
        drawLabel(
            f"{app.players[playerId].name}",
            app.width - landColWidth - armyColWidth - playerColWidth / 2,
            (i + 1) * rowHeight + rowHeight / 2,
            fill="black",
            align="center",
            size=14,
        )

        drawLabel(
            f"{app.board.countTroops(playerId)}",
            app.width - landColWidth - armyColWidth / 2,
            (i + 1) * rowHeight + rowHeight / 2,
            fill="black",
            align="center",
            size=14,
        )

        drawLabel(
            f"{app.board.countLand(playerId)}",
            app.width - landColWidth / 2,
            (i + 1) * rowHeight + rowHeight / 2,
            fill="black",
            align="center",
            size=14,
        )
