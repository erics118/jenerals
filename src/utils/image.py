def getImagePath(t, isVisible):
    """Get the image path of the cell to be used when drawing"""
    if not isVisible and t in ["city", "mountain"]:
        t = "obstacle"

    imageName = None
    match t:
        case "city":
            # image from https://generals.io/city.png
            imageName = "city"
        case "general":
            # image from https://generals.io/crown.png
            imageName = "crown"
        case "mountain":
            # image from https://generals.io/mountain.png
            imageName = "mountain"
        case "obstacle":
            # image from https://generals.io/obstacle.png
            imageName = "obstacle"

    if imageName is None:
        return None
    else:
        return f"./images/{imageName}.png"
