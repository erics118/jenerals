from .legal import isMoveLegal


def clearPremoves(app):
    app.premoves.clear()
    app.selectedCoords = app.premoveSelectedCoords


def doPremove(app, drow, dcol):
    # disregard illegal moves or if no cell is focused
    if not app.isFocused or not isMoveLegal(app, app.premoveSelectedCoords, drow, dcol):
        return

    new = (app.premoveSelectedCoords[0] + drow, app.premoveSelectedCoords[1] + dcol)

    # record the premove
    app.premoves.append((drow, dcol))

    app.premoveSelectedCoords = new
