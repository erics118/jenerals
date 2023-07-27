from objects.cell import getCellCoords


# on a mouse press, get the cell that was clicked on
def mousePress(app, mouseX, mouseY):
    coords = getCellCoords(app, mouseX, mouseY)
    if coords is None:
        return
    if coords == app.selectedCoords:
        app.isFocused = not app.isFocused
    else:
        app.isFocused = True
        app.selectedCoords = coords
