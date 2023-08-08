from cmu_graphics import *

from events.appStart import appStart
from events.drawAll import drawAll
from events.keyPress import keyPress
from events.mouseDrag import mouseDrag
from events.mousePress import mousePress
from events.mouseRelease import mouseRelease
from events.step import step
from utils.args import parseArgs

# moving:
# TODO: move instantly when have no premoves
# TODO: do premoves instantly if start and end pos both aren't player cells

# multiplayer:
# TODO: scoreboard
# TODO: sockets
# TODO: chat, put all notifications in there too
# TODO: capture general should end game

# other features:
# TODO: end game
# TODO: restart game
# TODO: z and click twice to take 50% troops
# TODO: surrender
# TODO: tutorial
# TODO: zooming


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
    args = parseArgs()
    dev = args.dev

    runApp(dev=dev)
