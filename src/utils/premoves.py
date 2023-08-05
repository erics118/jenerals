from utils.legal import isCoordLegal


def popPremove(app):
    """
    Remove the most recent premove
    """
    if len(app.premoves) > 0:
        app.premoves.pop()
        app.premoveSelectedCoords = app.premoves[-1][0]


def clearPremoves(app):
    """
    Clears the premove list and resets the premoveSelectedCoords
    """
    app.premoves.clear()
    app.selectedCoords = app.premoveSelectedCoords


def doPremove(app, newCoords, moveTroops=True):
    """
    Performs a premove if it is legal and updates the premoveSelectedCoords
    """

    # disregard illegal moves
    if not isCoordLegal(app, newCoords):
        return

    if app.premoveSelectedCoords is None:
        app.premoveSelectedCoords = app.selectedCoords

    # record the premove
    should = None
    if moveTroops == False:
        should = False
    elif moveTroops == True:
        if app.isFocused:
            should = True
        else:
            should = False

    app.premoves.append((newCoords, should))

    app.premoveSelectedCoords = newCoords
