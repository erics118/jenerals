def mousePress(app, mouseX, mouseY):
    """Handle mouse presses"""

    # check buttons first
    if app.button.isMouseWithin(mouseX, mouseY):
        return

    app.mouseCoords = (mouseX, mouseY)

    if app.hasOngoingGame:
        inGameMousePress(app, mouseX, mouseY)
    else:
        startScreenMousePress(app, mouseX, mouseY)


def startScreenMousePress(app, mouseX, mouseY):
    """Handle mouse presses on the start screen"""

    pass


def inGameMousePress(app, mouseX, mouseY):
    """Handle mouse presses in the game"""
    pass
