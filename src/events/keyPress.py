from utils.legal import isMoveLegal


def doPremove(app, drow, dcol):
    # disregard illegal moves or if no cell is focused
    if not app.isFocused or not isMoveLegal(app, app.premoveSelectedCoords, drow, dcol):
        return

    new = (app.premoveSelectedCoords[0] + drow, app.premoveSelectedCoords[1] + dcol)

    # record the premove
    app.premoves.append((drow, dcol))
    app.premoveSelectedCoords = new


# on a key press
def keyPress(app, key):
    # if space is pressed, toggle focus
    if key == "space":
        app.isFocused = not app.isFocused
    # if an arrow key is pressed, do a premove
    if key in ["up", "down", "left", "right"]:
        if key == "left":
            drow, dcol = 0, -1
        elif key == "right":
            drow, dcol = 0, 1
        elif key == "up":
            drow, dcol = -1, 0
        elif key == "down":
            drow, dcol = 1, 0
        doPremove(app, drow, dcol)


# TODO: key hold
