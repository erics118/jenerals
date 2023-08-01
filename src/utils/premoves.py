from .addTuple import add
from .legal import isMoveLegal


def popPremove(app):
    """
    Remove the most recent premove
    """
    if len(app.premoves) > 0:
        popped = app.premoves.pop()
        undo = (-popped[0], -popped[1])
        app.premoveSelectedCoords = add(app.premoveSelectedCoords, undo)


def clearPremoves(app):
    """
    Clears the premove list and resets the premoveSelectedCoords
    """
    app.premoves.clear()
    app.selectedCoords = app.premoveSelectedCoords


def doPremove(app, moveCoords):
    """
    Performs a premove if it is legal and updates the premoveSelectedCoords
    """

    # disregard illegal moves or if no cell is focused
    if not app.isFocused or not isMoveLegal(
        app, app.premoveSelectedCoords, moveCoords
    ):
        return

    new = add(app.premoveSelectedCoords, moveCoords)

    # record the premove
    app.premoves.append(moveCoords)

    app.premoveSelectedCoords = new
