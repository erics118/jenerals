import sys

from cmu_graphics import *

from events.appStart import appStart
from events.drawAll import drawAll
from events.keyPress import keyPress
from events.mouseDrag import mouseDrag
from events.mouseRelease import mouseRelease
from events.mousePress import mousePress
from events.step import step
from utils.cliFlags import ArgsConfig, parse

# NOTE: if not focused on a cell, still do premoves and dont move immediately

# TODO: if not focused on a cell, then allow for moving through mountains, enemy, etc
# TODO: broken when premoving into a mountain
# TODO: scoreboard
# TODO: chat, put all notifications in there too
# TODO: zoom in/out shortcuts
# TODO: allow taking 50% of troops
# TODO: ai
# TODO: flood fill to check if any place is blocked off
# TODO: restart game
# TODO: nicer pre-game screen
# TODO: allow player to play with another player with WASD


def onAppStart(app, dev=False):
    appStart(app, dev)


def onKeyPress(app, key):
    keyPress(app, key)


def redrawAll(app):
    drawAll(app)


def onMousePress(app, mouseX, mouseY):
    mousePress(app, mouseX, mouseY)


def onMouseRelease(app, mouseX, mouseY):
    mouseRelease(app, mouseX, mouseY)


def onMouseDrag(app, mouseX, mouseY):
    mouseDrag(app, mouseX, mouseY)


def onStep(app):
    step(app)


if __name__ == "__main__":
    # dev mode
    res = parse(sys.argv[1:], ArgsConfig(short=["d"], long="dev"))
    dev = res.get("d", False) or res.get("dev", False)

    runApp(dev=dev, width=600, height=600)
