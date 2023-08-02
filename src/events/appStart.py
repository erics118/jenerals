from cmu_graphics import *
from PIL import Image

from classes.board import Board
from classes.button import Button
from utils.colors import Colors
from utils.image import getImagePath


def newGame(app):
    """Create a new game"""

    app.buttons["play"].drawing = False

    app.hasOngoingGame = True
    app.isPaused = False
    app.forceIsVisible = False

    app.mouseCoords = None

    app.board = Board(app, 20, 20)
    app.board.step("visible")
    app.board.step("city")
    app.isFocused = True

    app.premoves = []

    app.c = 0


def appStart(app, dev):
    """Start the app"""

    # static values
    app.width = 800
    app.height = 800
    app.stepsPerSecond = 2
    app.cellBorderWidth = 0.8

    # is developer mode flag
    app.dev = dev

    # used to check something is working while developing
    app.flag = False

    # dragging
    app.isDragging = False

    # game
    app.hasOngoingGame = False
    app.cellSize = 32

    # buttons
    app.pressedButtonName = None

    app.buttons = {
        "play": Button(
            400,
            440,
            170,
            60,
            text="PLAY",
            onClick=newGame,
            textColor=Colors.ACCENT,
            textSize=22,
        )
    }

    # load all images, for visible and not visible
    app.images = {}

    # CITE: uses image from https://generals.io/city.png
    # CITE: uses image from https://generals.io/crown.png
    # CITE: uses image from https://generals.io/mountain.png
    # CITE: uses image from https://generals.io/obstacle.png
    # CITE: uses image from https://generals.io/swamp.png

    for t in ["city", "crown", "mountain", "obstacle", "swamp"]:
        # get the image
        image = Image.open(getImagePath(t))

        # resize the image
        imageSize = app.cellSize * 0.8
        image.thumbnail((imageSize, imageSize))

        # save the image
        app.images[t] = CMUImage(image)
