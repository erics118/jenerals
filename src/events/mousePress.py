# on a mouse press, get the cell that was clicked on
def mousePress(app, mouseX, mouseY):
    if app.hasOngoingGame:
        inGameMousePress(app, mouseX, mouseY)
    else:
        startScreenMousePress(app, mouseX, mouseY)


def inGameMousePress(app, mouseX, mouseY):
    app.mx, app.my = mouseX, mouseY


def startScreenMousePress(app, mouseX, mouseY):
    pass
