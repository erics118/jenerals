from objects.cell import getCellCoords


# on a mouse press, get the cell that was clicked on
def mouseRelease(app, mouseX, mouseY):
    if app.hasOngoingGame:
        inGameMouseRelease(app, mouseX, mouseY)
    else:
        startScreenMouseRelease(app, mouseX, mouseY)


def inGameMouseRelease(app, mouseX, mouseY):
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


def startScreenMouseRelease(app, mouseX, mouseY):
    pass
