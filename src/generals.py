from cmu_graphics import *
from events.appStart import appStart
from events.drawAll import drawAll
from events.keyPress import keyPress
from events.mouseDrag import mouseDrag
from events.mousePress import mousePress
from events.step import step

# TODO: if not focused on a cell, then dont do premoves
# TODO: if not focused on a cell, then allow for moving through mountains, enemy, etc
# TODO: scoreboard
# TODO: chat, put all notifications in there too
# TODO: zoom in/out shortcuts
# TODO: allow taking 50% of troops
# TODO: dev gather all troops
# TODO: make all cells visible
# TODO: ai
# TODO: restart game
# TODO: pre-game screen
# TODO: allow player to play with another player with WASD


def onAppStart(app):
    appStart(app)


def onKeyPress(app, key):
    keyPress(app, key)


def redrawAll(app):
    drawAll(app)


def onMousePress(app, mouseX, mouseY):
    mousePress(app, mouseX, mouseY)


def onMouseDrag(app, mouseX, mouseY):
    mouseDrag(app, mouseX, mouseY)


def onStep(app):
    if app.isPaused:
        return
    step(app)


runApp(width=600, height=600)
