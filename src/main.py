import sys

from cmu_graphics import *

from events.appStart import appStart
from events.drawAll import drawAll
from events.keyPress import keyPress
from events.mouseDrag import mouseDrag
from events.mousePress import mousePress
from events.mouseRelease import mouseRelease
from events.step import step
from utils.cliFlags import ArgsConfig, parse

# TODO: if not focused on a cell, then allow for moving through mountains, enemy, etc
# TODO: broken when premoving into a mountain
# TODO: scoreboard
# TODO: chat, put all notifications in there too
# TODO: zoom in/out shortcuts
# TODO: allow taking 50% of troops
# TODO: restart game
# TODO: allow player to play with another player with WASD
# TODO: somehow increase the resolution
# TODO: shift to move mask (meaning only change focus)
# TODO: z and click twice to take 50% troops
# TODO: fix clicking when having premoves


def onAppStart(app, dev=False):
    """Initializes the application when it starts."""
    appStart(app, dev)


def onKeyPress(app, key):
    """Handle key presses"""
    keyPress(app, key)


def redrawAll(app):
    """Draw all elements of the app"""
    drawAll(app)


def onMousePress(app, mouseX, mouseY):
    """Handle mouse presses"""
    mousePress(app, mouseX, mouseY)


def onMouseRelease(app, mouseX, mouseY):
    """Handle mouse releases"""
    mouseRelease(app, mouseX, mouseY)


def onMouseDrag(app, mouseX, mouseY):
    """Handle mouse drags"""
    mouseDrag(app, mouseX, mouseY)


def onStep(app):
    """Handle step events"""
    step(app)


if __name__ == "__main__":
    # dev mode
    res = parse(sys.argv[1:], ArgsConfig(short=["d"], long="dev"))
    dev = res.get("d", False) or res.get("dev", False)

    runApp(dev=dev)
