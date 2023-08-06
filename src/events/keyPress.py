from classes.move import Move
from events.appStart import newGame
from events.step import stepWithCount
from utils.premoves import addPremove, clearPremoves, popPremove
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

        # if an arrow key is pressed, do a premove
        case "left":
            addPremove(
                0, app, Move(add(app.players[0].premoveSelectedCoords, (0, -1)))
            )
        case "right":
            addPremove(
                0, app, Move(add(app.players[0].premoveSelectedCoords, (0, 1)))
            )
        case "up":
            addPremove(
                0, app, Move(add(app.players[0].premoveSelectedCoords, (-1, 0)))
            )
        case "down":
            addPremove(
                0, app, Move(add(app.players[0].premoveSelectedCoords, (1, 0)))
            )
        case "a":
            addPremove(
                1, app, Move(add(app.players[1].premoveSelectedCoords, (0, -1)))
            )
        case "d":
            addPremove(
                1, app, Move(add(app.players[1].premoveSelectedCoords, (0, 1)))
            )
        case "w":
            addPremove(
                1, app, Move(add(app.players[1].premoveSelectedCoords, (-1, 0)))
            )
        case "s":
            addPremove(
                1, app, Move(add(app.players[1].premoveSelectedCoords, (1, 0)))
            )
        # if q is pressed, clear premoves
        case "i":
            clearPremoves(0, app)
        case "p":
            popPremove(0, app)
        case "l":
            app.players[0].isFocused ^= True
        case "q":
            clearPremoves(1, app)
        case "e":
            popPremove(1, app)
        case "z":
            app.players[1].isFocused ^= True

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
        # case "?":
        #     while len(app.premoves) >= 1:
        #         doMove(app, app.premoves.pop(0))
        case "P":
            app.isPaused = not app.isPaused
        case "V":
            app.forceIsVisible = not app.forceIsVisible


# TODO: key hold
