from utils.legal import isCoordLegal


def popPremove(app):
    """
    Remove the most recent premove
    """
    if len(app.premoves) > 0:
        app.premoves.pop()
        app.premoveSelectedCoords = app.premoves[-1]


def clearPremoves(app):
    """
    Clears the premove list and resets the premoveSelectedCoords
    """
    app.premoves.clear()
    app.selectedCoords = app.premoveSelectedCoords


def doPremove(app, newCoords):
    """
    Performs a premove if it is legal and updates the premoveSelectedCoords
    """

    # disregard illegal moves
    if not isCoordLegal(app, newCoords):
        return

    if app.premoveSelectedCoords is None:
        app.premoveSelectedCoords = app.selectedCoords

    # record the premove
    app.premoves.append(newCoords)

    app.premoveSelectedCoords = newCoords
