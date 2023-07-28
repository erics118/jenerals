from utils.legal import isMoveLegal
from utils.premoves import clearPremoves
from .step import stepWithCount, doMove


# TODO: make premove show the selected cell as well and be instant rather than onStep
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
    match key:
        # if space is pressed, toggle focus
        case "space":
            app.isFocused = not app.isFocused
        # if an arrow key is pressed, do a premove
        case "left":
            doPremove(app, 0, -1)
        case "right":
            doPremove(app, 0, 1)
        case "up":
            doPremove(app, -1, 0)
        case "down":
            doPremove(app, 1, 0)
        # if q is pressed, clear premoves
        case "q":
            clearPremoves(app)
        # dev stuff
        # toggle flag
        case ",":
            app.flag = not app.flag
        # step once
        case ".":
            stepWithCount(app)
        # step 100 times
        case ">":
            for _ in range(50):
                stepWithCount(app)
        # do all premoves
        case "/":
            # TODO: can go thru mountains with this
            while len(app.premoves) >= 1:
                doMove(app, *app.premoves.pop(0))
        case "p":
            app.isPaused = not app.isPaused


# TODO: key hold
