from utils.legal import isMoveLegal


def popPremove(app):
    """
    Remove the most recent premove
    """
    if len(app.premoves) > 0:
        app.premoves.pop()
        app.premoveSelectedCoords = app.premoves[-1].coords


def clearPremoves(app):
    """
    Clears the premove list and resets the premoveSelectedCoords
    """
    app.premoves.clear()
    app.selectedCoords = app.premoveSelectedCoords


def doPremove(app, move):
    """
    Performs a premove if it is legal and updates the premoveSelectedCoords
    """

    # disregard illegal moves
    if not isMoveLegal(app, move):
        return

    if app.premoveSelectedCoords is None:
        app.premoveSelectedCoords = app.selectedCoords

    # record the premove
    if move.moveTroops == False:
        move.moveTroops = False
    elif move.moveTroops == True:
        if app.isFocused:
            move.moveTroops = True
        else:
            move.moveTroops = False

    app.premoves.append(move)

    app.premoveSelectedCoords = move.coords
