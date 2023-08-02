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

# moving:
# TODO: if not focused on a cell, then allow for moving through mountains, enemy, etc
# TODO: fix clicking when having premoves
# TODO: move instantly when have no premoves
# TODO: broken when premoving into a mountain

# multiplayer:
# TODO: scoreboard
# TODO: sockets
# TODO: allow player to play with another player with WASD
# TODO: chat, put all notifications in there too

# other features:
# TODO: end game
# TODO: restart game
# TODO: somehow increase the resolution
# TODO: z and click twice to take 50% troops


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
