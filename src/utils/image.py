import os
import pathlib

# CITE: uses images from:
#     https://generals.io/city.png
#     https://generals.io/crown.png
#     https://generals.io/mountain.png
#     https://generals.io/obstacle.png
#     https://generals.io/swamp.png


# CITE: modified from graphics demos provided on Piazza
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
