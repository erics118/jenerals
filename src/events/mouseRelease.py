from classes.cell import getCellCoords


def mouseRelease(app, mouseX, mouseY):
    """Handle mouse releases"""

    if app.hasOngoingGame:
        inGameMouseRelease(app, mouseX, mouseY)
    else:
        startScreenMouseRelease(app, mouseX, mouseY)


def startScreenMouseRelease(app, mouseX, mouseY):
    """Handle mouse releases on the start screen"""
    pass


def inGameMouseRelease(app, mouseX, mouseY):
    """Handle mouse releases in the game"""

    if not app.isDragging:
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
    app.isDragging = False
