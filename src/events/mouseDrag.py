def mouseDrag(app, mouseX, mouseY):
    if app.hasOngoingGame:
        inGameMouseDrag(app, mouseX, mouseY)
    else:
        startScreenMouseDrag(app, mouseX, mouseY)


def inGameMouseDrag(app, mouseX, mouseY):
    app.isDragging = True
    app.board.left = mouseX - app.mx + app.board.left
    app.board.top = mouseY - app.my + app.board.top
    app.mx, app.my = mouseX, mouseY


def startScreenMouseDrag(app, mouseX, mouseY):
    pass
