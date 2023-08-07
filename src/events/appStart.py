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
    app.buttons["replay"].drawing = False
    app.buttons["exit"].drawing = False

    app.hasOngoingGame = True
    app.isPaused = False
    app.ended = False
    app.winnerId = None

    app.forceIsVisible = True

    app.mouseCoords = None

    app.players = [
        Player(0, "blue bruh", Colors.BLUE),
        Player(1, "red bro", Colors.RED),
    ]

    app.board = Board(app, 20, 20)
    app.board.step("visible")
    app.board.step("city")

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

    def goToStartScreen(app):
        app.hasOngoingGame = False
        app.buttons["play"].drawing = True
        app.buttons["replay"].drawing = False
        app.buttons["exit"].drawing = False

    app.buttons = {
        "play": Button(
            400,
            440,
            170,
            60,
            text="Play",
            onClick=newGame,
            textColor=Colors.ACCENT,
            textSize=22,
        ),
        "replay": Button(
            400,
            400,
            140,
            50,
            text="Replay",
            onClick=newGame,
            textColor=Colors.WHITE,
            textSize=18,
            fill=Colors.ACCENT,
            accent=Colors.BACKGROUND,
            drawing=False,
        ),
        "exit": Button(
            400,
            470,
            140,
            50,
            text="Exit",
            onClick=goToStartScreen,
            textColor=Colors.WHITE,
            textSize=18,
            fill=Colors.ACCENT,
            accent=Colors.BACKGROUND,
            drawing=False,
        ),
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
