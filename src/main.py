from cmu_graphics import *

from events.appStart import appStart
from events.drawAll import drawAll
from events.keyPress import keyPress
from events.mouseDrag import mouseDrag
from events.mousePress import mousePress
from events.mouseRelease import mouseRelease
from events.step import step
from utils.args import parseArgs
from utils.ip import encodeIp

from utils.sockets import makePrimarySocket, makeSecondarySocket

# TODO: move without premoves when not focused
# currently, premoves still show even though the unfocused move is instant
# TODO: wait for both players to be ready before starting


def onAppStart(app, socket, ip, identity, dev=False):
    """Initializes the application when it starts."""
    appStart(app, socket, ip, identity, dev)


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

    if args.primary:
        socket, ip, identity = makePrimarySocket()

    if args.secondary:
        socket, ip, identity = makeSecondarySocket(args.code)

    print()
    print(f"! Room Code: {encodeIp(ip)}")
    print(f"! Identity: {identity}")
    print()

    runApp(
        socket=socket,
        ip=ip,
        identity=identity,
        dev=dev,
    )
