from classes.cell import getCellCoords


def mouseRelease(app, mouseX, mouseY):
    """Handle mouse releases"""

    # stop dragging if is dragging
    if app.isDragging:
        app.isDragging = False
        app.mouseCoords = None
        return

    # check if clicked on button
    if app.button.checkClick(mouseX, mouseY):
        return

    if app.hasOngoingGame:
        inGameMouseRelease(app, mouseX, mouseY)
    else:
        startScreenMouseRelease(app, mouseX, mouseY)


def startScreenMouseRelease(app, mouseX, mouseY):
    """Handle mouse releases on the start screen"""
    pass


def inGameMouseRelease(app, mouseX, mouseY):
    """Handle mouse releases in the game"""

    coords = getCellCoords(app, mouseX, mouseY)
    if coords is None:
        return
    if coords == app.selectedCoords:
        app.isFocused = not app.isFocused
    else:
        app.isFocused = True
        if app.premoveSelectedCoords == app.selectedCoords:
            app.premoveSelectedCoords = coords
        app.selectedCoords = coords
