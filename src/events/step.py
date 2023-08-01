from utils.addTuple import add
from utils.legal import isMoveLegal
from utils.premoves import clearPremoves


def doMove(app, moveCoords):
    """Move troops from one cell to another"""

    # disregard illegal moves or if no cell is focused
    if not app.isFocused or not isMoveLegal(
        app, app.selectedCoords, moveCoords
    ):
        # clear remaining premoves that follow that illegal move
        clearPremoves(app)
        return

    newCoords = add(app.selectedCoords, moveCoords)
    new = app.board.at(newCoords)
    selected = app.board.at(app.selectedCoords)

    # if selected is player
    if selected.team == "player":
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
                    new.team = "player"
                    new.isVisible = True
                else:
                    clearPremoves(app)

            elif new.t == "city":
                # capturing a city consumes the numTroops the city has
                if selected.numTroops >= new.numTroops + 1:
                    # then move the troops over, leaving one behind and using one up
                    new.numTroops = selected.numTroops - new.numTroops - 2
                    # old cell has two troops left
                    selected.numTroops = 1
                    # new cell is now player
                    new.team = "player"
                    new.isVisible = True
                # otherwise, not enough troops to capture it. send all the troops over anyway
                else:
                    new.numTroops = new.numTroops - selected.numTroops + 1
                    selected.numTroops = 1
                    clearPremoves(app)

        # elif is own cell
        elif new.team == "player":
            if selected.numTroops == 1 and new.numTroops == 1:
                return

            # then move the troops over, leaving one behind
            new.numTroops += selected.numTroops - 1
            # old cell has one troop left
            selected.numTroops = 1

    if selected.team == "neutral":
        if new.team == "player":
            app.selectedCoords = newCoords
            app.premoveSelectedCoords = newCoords

    app.selectedCoords = newCoords


def stepWithCount(app):
    """
    A step occurs twice a second.
    A turn is two steps.
    Every step, cities and generals step.
    Every 25 steps, all cells step.
    """

    app.c += 1
    if app.c % (app.stepsPerSecond * 25) == 0:
        app.board.step("all")
    elif app.c % (app.stepsPerSecond) == 0:
        app.board.step("city")


def step(app):
    """Handle step events"""

    if not app.hasOngoingGame:
        return

    if app.isPaused:
        return

    if len(app.premoves) >= 1:
        doMove(app, app.premoves.pop(0))

    stepWithCount(app)
