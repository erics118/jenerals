from objects.cell import getCell


def mousePress(app, mouseX, mouseY):
    x, y = getCell(app, mouseX, mouseY)
    if (x, y) == app.selectedCell:
        app.isFocused = not app.isFocused
    else:
        app.isFocused = True
        app.selectedCell = (x, y)
