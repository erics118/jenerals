import os
import pathlib
from cmu_graphics import CMUImage
from PIL import Image, ImageFilter

# CITE: uses images from:
#     https://generals.io/city.png
#     https://generals.io/crown.png
#     https://generals.io/mountain.png
#     https://generals.io/obstacle.png
#     https://generals.io/swamp.png


# CITE: modified from graphics demos provided on Piazza
def getImagePath(imageName):
    """Get the image path of the cell to be used when drawing"""

    return os.path.join(pathlib.Path(__file__).parent, f"../../images/{imageName}.png")


def getImage(app, t, isVisible):
    """Get the image of the cell to be used when drawing"""

    imageName = t

    if t == "general":
        imageName = "crown" if isVisible else None

    if (not isVisible) and (t in ["city", "mountain"]):
        imageName = "obstacle"

    return app.images.get(imageName)


def loadImages(app):
    """Load the images"""
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
