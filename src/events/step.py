from utils.premoves import clearPremoves
from utils.legal import isMoveLegal


def doMove(app, drow, dcol):
    # disregard illegal moves or if no cell is focused
    if not app.isFocused or not isMoveLegal(app, app.selectedCoords, drow, dcol):
        # clear remaining premoves that follow that illegal move
        clearPremoves(app)
        return

    new = (app.selectedCoords[0] + drow, app.selectedCoords[1] + dcol)

    # if selected is player
    if app.board.at(*app.selectedCoords).team == "player":
        # if new cell is neutral
        if app.board.at(*new).team == "neutral":
            # the selected cell has at more than one troop
            if app.board.at(*app.selectedCoords).numTroops > 1:
                # then move the troops over, leaving one behind and using one up
                app.board.at(*new).numTroops += (
                    app.board.at(*app.selectedCoords).numTroops - 1
                )
                # old cell has one troop left
                app.board.at(*app.selectedCoords).numTroops = 1
                # new cell is now player
                app.board.at(*new).team = "player"

        # elif is own cell
        elif app.board.at(*new).team == "player":
            if (
                app.board.at(*app.selectedCoords).numTroops == 1
                and app.board.at(*new).numTroops == 1
            ):
                return

            # then move the troops over, leaving one behind
            app.board.at(*new).numTroops += (
                app.board.at(*app.selectedCoords).numTroops - 1
            )
            # old cell has one troop left
            app.board.at(*app.selectedCoords).numTroops = 1

    app.selectedCoords = new


def stepWithCount(app):
    app.c += 1
    if app.c % (app.stepsPerSecond * 25) == 0:
        app.board.step("all")
    elif app.c % (app.stepsPerSecond) == 0:
        app.board.step("city")


def step(app):
    if len(app.premoves) >= 1:
        doMove(app, *app.premoves.pop(0))

    stepWithCount(app)
