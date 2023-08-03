from .legal import isCoordLegal


def popPremove(app):
    """
    Remove the most recent premove
    """
    if len(app.premoves) > 0:
        app.premoveSelectedCoords = app.premoves.pop()
        # undo = (-popped[0], -popped[1])
        # app.premoveSelectedCoords = add(app.premoveSelectedCoords, undo)


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

    # record the premove
    app.premoves.append(newCoords)

    app.premoveSelectedCoords = newCoords
