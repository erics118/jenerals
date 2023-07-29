def mousePress(app, mouseX, mouseY):
    """Handle mouse presses"""

    if app.hasOngoingGame:
        inGameMousePress(app, mouseX, mouseY)
    else:
        startScreenMousePress(app, mouseX, mouseY)


def startScreenMousePress(app, mouseX, mouseY):
    """Handle mouse presses on the start screen"""

    pass


def inGameMousePress(app, mouseX, mouseY):
    """Handle mouse presses in the game"""

    app.mx, app.my = mouseX, mouseY
