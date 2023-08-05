from utils.legal import isMoveLegal


def popPremove(app):
    """
    Remove the most recent premove
    """
    if len(app.premoves) > 0:
        app.premoves.pop()
        app.premoveSelectedCoords = app.premoves[-1].coords


def clearPremoves(playerId, app):
    """
    Clears the premove list and resets the premoveSelectedCoords
    """
    app.players[playerId].premoves.clear()
    app.players[playerId].selectedCoords = app.players[
        playerId
    ].premoveSelectedCoords


def doPremove(playerId, app, move):
    """
    Performs a premove if it is legal and updates the premoveSelectedCoords
    """

    # disregard illegal moves
    if not isMoveLegal(playerId, app, move):
        return

    if app.players[playerId].premoveSelectedCoords is None:
        app.players[playerId].premoveSelectedCoords = app.players[
            playerId
        ].selectedCoords

    # record the premove
    if move.moveTroops == False:
        move.moveTroops = False
    elif move.moveTroops == True:
        if app.players[playerId].isFocused:
            move.moveTroops = True
        else:
            move.moveTroops = False

    app.players[playerId].premoves.append(move)

    app.players[playerId].premoveSelectedCoords = move.coords
