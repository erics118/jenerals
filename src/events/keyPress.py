from events.appStart import newGame
from events.step import doMove, stepWithCount
from utils.premoves import clearPremoves, doPremove, popPremove
from utils.tuple import add


def keyPress(app, key):
    """Handle key presses"""

    if not app.hasOngoingGame:
        startScreenKeyPress(app, key)
    else:
        inGameKeyPress(app, key)


def startScreenKeyPress(app, key):
    """Handle key presses on the start screen"""

    match key:
        case "enter":
            newGame(app)


def inGameKeyPress(app, key):
    """Handle key presses in the game"""

    match key:
        # if space is pressed, toggle focus
        case "space":
            app.isFocused = not app.isFocused
        # if an arrow key is pressed, do a premove
        case "left":
            doPremove(app, add(app.premoveSelectedCoords, (0, -1)))
        case "right":
            doPremove(app, add(app.premoveSelectedCoords, (0, 1)))
        case "up":
            doPremove(app, add(app.premoveSelectedCoords, (-1, 0)))
        case "down":
            doPremove(app, add(app.premoveSelectedCoords, (1, 0)))
        # if q is pressed, clear premoves
        case "q":
            clearPremoves(app)
        case "e":
            popPremove(app)

    if app.dev:
        devKeyPress(app, key)


def devKeyPress(app, key):
    """Handle key presses in the game when dev mode is on"""

    match key:
        # toggle flag
        case "F":
            app.flag = not app.flag
        # step once
        case "<":
            stepWithCount(app)
        # step 25 turns
        case ">":
            for _ in range(app.stepsPerSecond * 25 * 2):
                stepWithCount(app)
        # do all premoves
        case "?":
            while len(app.premoves) >= 1:
                doMove(app, app.premoves.pop(0)[0])
        case "P":
            app.isPaused = not app.isPaused
        case "V":
            app.forceIsVisible = not app.forceIsVisible
        case "C":
            app.board.collectTroops(app.selectedCoords)


# TODO: key hold
