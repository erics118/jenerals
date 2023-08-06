from classes.cell import getCellCoords


def mouseRelease(app, mouseX, mouseY):
    """Handle mouse releases"""

    # stop dragging if is dragging
    if app.isDragging:
        app.isDragging = False
        app.mouseCoords = None
        return

    # on mouse release, check if the button that was pressed down in mousePress
    # is the same as the button that is being released
    # if so, call the button's click method
    # if the release position isn't even a button, do nothing
    if app.pressedButtonName is not None:
        if app.buttons[app.pressedButtonName].isMouseWithin(mouseX, mouseY):
            app.buttons[app.pressedButtonName].click()
        app.pressedButtonName = None
        return

    if app.hasOngoingGame:
        inGameMouseRelease(app, mouseX, mouseY)
    else:
        startScreenMouseRelease(app, mouseX, mouseY)


def startScreenMouseRelease(_app, _mouseX, _mouseY):
    """Handle mouse releases on the start screen"""


# TODO: do this after sockets are done
def inGameMouseRelease(app, mouseX, mouseY):
    """Handle mouse releases in the game"""

    coords = getCellCoords(app, mouseX, mouseY)
    if coords is None:
        return
    if coords == app.selectedCoords:
        app.isFocused = not app.isFocused
    else:
        app.isFocused = True

        # addPremove(1, app, Move(coords, False))
