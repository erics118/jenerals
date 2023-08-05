from utils.legal import isMoveLegal
from utils.premoves import clearPremoves


def doMove(playerId, app, move):
    """Move troops from one cell to another"""

    p = app.players[playerId]
    # disregard illegal moves or if no cell is focused
    if not p.isFocused or not isMoveLegal(playerId, app, move):
        # clear remaining premoves that follow that illegal move
        clearPremoves(playerId, app)
        return

    new = app.board.at(move.coords)
    selected = app.board.at(p.selectedCoords)

    if move.moveTroops:
        # if selected is player
        if selected.team == f"player{playerId}":
            # if new cell is neutral
            if new.team == "neutral":
                if new.t == "fog":
                    # the selected cell has at more than one troop
                    if selected.numTroops > 1:
                        # then move the troops over, leaving one behind and using one up
                        new.numTroops += selected.numTroops - 1
                        # old cell has one troop left
                        selected.numTroops = 1
                        # new cell is now player
                        new.team = f"player{playerId}"
                        new.isVisible = True
                    else:
                        clearPremoves(playerId, app)

                elif new.t == "city":
                    # capturing a city consumes the numTroops the city has
                    if selected.numTroops >= new.numTroops + 1:
                        # then move the troops over, leaving one behind and using one up
                        new.numTroops = selected.numTroops - new.numTroops - 2
                        # old cell has two troops left
                        selected.numTroops = 1
                        # new cell is now player
                        new.team = f"player{playerId}"
                        new.isVisible = True
                    # otherwise, not enough troops to capture it. send all the troops over anyway
                    else:
                        new.numTroops = new.numTroops - selected.numTroops + 1
                        selected.numTroops = 1
                        clearPremoves(playerId, app)

            # elif is own cell
            elif new.team == f"player{playerId}":
                if selected.numTroops == 1 and new.numTroops == 1:
                    return

                # then move the troops over, leaving one behind
                new.numTroops += selected.numTroops - 1
                # old cell has one troop left
                selected.numTroops = 1
            # elif is opponent
            elif new.team.startswith("player"):
                if selected.numTroops == new.numTroops + 1:
                    # that cell becomes 0
                    new.numTroops = 0
                    selected.numTroops = 1
                elif selected.numTroops > new.numTroops + 1:
                    # then move the troops over, leaving one behind and using one up
                    new.numTroops = selected.numTroops - new.numTroops - 1
                    # old cell has two troops left
                    selected.numTroops = 1
                    # new cell is now player
                    new.team = f"player{playerId}"
                    new.isVisible = True
                # otherwise, not enough troops to capture it. send all the troops over anyway
                else:
                    new.numTroops = new.numTroops - selected.numTroops + 1
                    selected.numTroops = 1
                    clearPremoves(playerId, app)

    # if selected.team == "neutral":
    #     if new.team == "player":
    #         app.selectedCoords = newCoords
    #         app.premoveSelectedCoords = newCoords

    app.players[playerId].selectedCoords = move.coords
    app.board.step("visible")


def stepWithCount(app):
    """
    A step occurs twice a second.
    A turn is two steps.
    Every turn, cities and generals step.
    Every 25 turns, all cells step.
    """

    app.c += 1

    if app.c % (25 * app.stepsPerSecond) == 0:
        app.board.step("all")
    elif app.c % (app.stepsPerSecond) == 0:
        app.board.step("city")


def step(app):
    """Handle step events"""

    if not app.hasOngoingGame:
        return

    if app.isPaused:
        return

    stepWithCount(app)

    if app.c % (app.stepsPerSecond // 2) == 0:
        for playerId, p in enumerate(app.players):
            if len(p.premoves) >= 1:
                doMove(playerId, app, p.premoves.pop(0))
