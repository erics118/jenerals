from classes.move import Move
from events.appStart import newGame
from events.step import doMove, stepWithCount
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
    otherPlayerId = 1 if app.identity == 0 else 0
    o = app.players[otherPlayerId]

    match key:
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

        case "a":
            addPremove(otherPlayerId, app, Move(add(o.premoveSelectedCoords, (0, -1))))
        case "d":
            addPremove(otherPlayerId, app, Move(add(o.premoveSelectedCoords, (0, 1))))
        case "w":
            addPremove(otherPlayerId, app, Move(add(o.premoveSelectedCoords, (-1, 0))))
        case "s":
            addPremove(otherPlayerId, app, Move(add(o.premoveSelectedCoords, (1, 0))))
        case "z":
            clearPremoves(otherPlayerId, app)
        case "x":
            popPremove(otherPlayerId, app)
        case "c":
            app.players[otherPlayerId].isFocused ^= True

    if app.dev:
        devKeyPress(app, key)


def devKeyPress(app, key):
    """Handle key presses in the game when dev mode is on"""

    match key:
        # toggle flag
        case "F":
            app.flag = not app.flag
        case "V":
            app.forceIsVisible = not app.forceIsVisible
        # step once
        case "<":
            # step twice, so one turn
            for _ in range(app.stepsPerSecond * 2):
                stepWithCount(app)
            app.msg.set("STEP-1")
        # step 25 turns
        case ">":
            for _ in range(app.stepsPerSecond * 25 * 2):
                stepWithCount(app)
            app.msg.set("STEP-25")
        # do all premoves
        case "?":
            p = app.players[app.identity]
            while len(p.premoves) >= 1:
                doMove(app.identity, app, p.premoves.pop(0))
            otherId = 1 if app.identity == 0 else 0
            o = app.players[otherId]
            while len(o.premoves) >= 1:
                doMove(otherId, app, o.premoves.pop(0))
        case "P":
            app.isPaused = not app.isPaused
