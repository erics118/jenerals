import os
import pathlib


def getImagePath(imageName):
    """Get the image path of the cell to be used when drawing"""

    return os.path.join(
        pathlib.Path(__file__).parent, f"../../images/{imageName}.png"
    )


def getImage(app, t, isVisible):
    """Get the image of the cell to be used when drawing"""

    imageName = t

    if t == "general":
        imageName = "crown"

    if (not isVisible) and (t in ["city", "mountain"]):
        imageName = "obstacle"

    return app.images.get(imageName)
