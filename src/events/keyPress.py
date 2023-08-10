from classes.move import Move
from events.appStart import newGame
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

    p = app.players[app.identity]
    match key:
        # if space is pressed, toggle focus

        # if an arrow key is pressed, do a premove
        case "left":
            addPremove(app.identity, app, Move(add(p.premoveSelectedCoords, (0, -1))))
        case "right":
            addPremove(app.identity, app, Move(add(p.premoveSelectedCoords, (0, 1))))
        case "up":
            addPremove(app.identity, app, Move(add(p.premoveSelectedCoords, (-1, 0))))
        case "down":
            addPremove(app.identity, app, Move(add(p.premoveSelectedCoords, (1, 0))))
        case "q":
            clearPremoves(app.identity, app)
        case "e":
            popPremove(app.identity, app)
        case "space":
            app.players[app.identity].isFocused ^= True

    if app.dev:
        devKeyPress(app, key)


def devKeyPress(app, key):
    """Handle key presses in the game when dev mode is on"""

    match key:
        # toggle flag
        case "F":
            app.flag = not app.flag
        # step once
        # case "<":
        #     # step twice, so one turn
        #     for _ in range(app.stepsPerSecond * 2):
        #         stepWithCount(app)
        #     app.msg.set("STEP-1")
        # # step 25 turns
        # case ">":
        #     for _ in range(app.stepsPerSecond * 25 * 2):
        #         stepWithCount(app)
        #     app.msg.set("STEP-25")
        # # do all premoves
        # case "?":
        #     p = app.players[app.identity]
        #     while len(p.premoves) >= 1:
        #         doMove(app.identity, app, p.premoves.pop(0))
        # case "P":
        #     app.isPaused = not app.isPaused
        case "V":
            app.forceIsVisible = not app.forceIsVisible
