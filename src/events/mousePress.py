from objects.cell import getCellCoords


# on a mouse press, get the cell that was clicked on
def mousePress(app, mouseX, mouseY):
    app.mx, app.my = mouseX, mouseY

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
