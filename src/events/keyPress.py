from utils.premoves import clearPremoves, doPremove
from .step import stepWithCount, doMove


# on a key press
def keyPress(app, key):
    if not app.hasOngoingGame:
        startScreenKeyPress(app, key)
    else:
        inGameKeyPress(app, key)


# key presses on start screen
def startScreenKeyPress(app, key):
    match key:
        case "enter":
            app.startGame()


def inGameKeyPress(app, key):
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

    if app.dev:
        devKeyPress(app, key)


# dev cheats
def devKeyPress(app, key):
    match key:
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
            # TODO: fix going through mountains with this
            while len(app.premoves) >= 1:
                doMove(app, *app.premoves.pop(0))
        case "p":
            app.isPaused = not app.isPaused
        case "v":
            app.forceIsVisible = not app.forceIsVisible
        case "r":
            app.board.collectTroops(app.selectedCoords)


# TODO: key hold
