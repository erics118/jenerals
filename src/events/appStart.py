from cmu_graphics import *
from PIL import Image, ImageFilter

from classes.board import Board
from classes.button import Button
from classes.player import Player
from utils.colors import Colors
from utils.image import getImagePath


def newGame(app):
    """Create a new game"""

    app.buttons["play"].drawing = False

    app.hasOngoingGame = True
    app.isPaused = False
    app.forceIsVisible = True

    app.mouseCoords = None

    app.players = [
        Player("Player 0", Colors.PLAYER_0),
        Player("Player 1", Colors.PLAYER_1),
    ]

    app.board = Board(app, 20, 20)
    app.board.step("visible")
    app.board.step("city")

    # app.isFocused = True

    # app.premoves = []

    # start at first turn
    app.c = 1 * app.stepsPerSecond


def appStart(app, dev):
    """Start the app"""

    # static values
    app.width = 800
    app.height = 800
    app.stepsPerSecond = 20
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

    for t in ["city", "crown", "mountain", "obstacle", "swamp"]:
        # get the image
        image = Image.open(getImagePath(t))
        # first convert to RGBA before sharpening, because sharpen doesn't work
        # when the image is in P mode
        # CITE: https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.convert

        image = image.convert("RGBA")
        # resize the image
        imageSize = app.cellSize * 0.8

        # CITE: https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.thumbnail
        image.thumbnail((imageSize, imageSize))

        # sharpen the image
        # doesn't really do much, but slightly darker lines
        # CITE: https://pillow.readthedocs.io/en/stable/reference/ImageFilter.html
        image = image.filter(ImageFilter.SHARPEN)

        # save the image
        app.images[t] = CMUImage(image)
