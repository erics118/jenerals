from utils.legal import isMoveLegal


def popPremove(playerId, app):
    """
    Remove the most recent premove
    """
    p = app.players[playerId]

    if len(p.premoves) > 0:
        p.premoves.pop()
        if len(p.premoves) == 0:
            p.premoveSelectedCoords = None
        else:
            p.premoveSelectedCoords = p.premoves[-1].coords


def clearPremoves(playerId, app):
    """
    Clears the premove list and resets the premoveSelectedCoords
    """
    p = app.players[playerId]

    p.premoves.clear()
    p.selectedCoords = p.premoveSelectedCoords


def addPremove(playerId, app, move):
    """
    Add premove if it is legal and updates the premoveSelectedCoords
    """

    p = app.players[playerId]

    # disregard illegal moves
    if not isMoveLegal(playerId, app, move):
        return

    if p.premoveSelectedCoords is None:
        p.premoveSelectedCoords = p.selectedCoords

    # record the premove
    if move.moveTroops:
        if p.isFocused:
            move.moveTroops = True
        else:
            move.moveTroops = False

    p.premoves.append(move)

    p.premoveSelectedCoords = move.coords
