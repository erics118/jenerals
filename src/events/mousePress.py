def mousePress(app, mouseX, mouseY):
    """Handle mouse presses"""

    # if clicked on a button, set pressedButtonId and return
    for buttonName, button in app.buttons.items():
        if button.isMouseWithin(mouseX, mouseY):
            app.pressedButtonName = buttonName
            return

    app.mouseCoords = (mouseX, mouseY)

    if app.hasOngoingGame:
        inGameMousePress(app, mouseX, mouseY)
    else:
        startScreenMousePress(app, mouseX, mouseY)


def startScreenMousePress(_app, _mouseX, _mouseY):
    """Handle mouse presses on the start screen"""


def inGameMousePress(_app, _mouseX, _mouseY):
    """Handle mouse presses in the game"""
