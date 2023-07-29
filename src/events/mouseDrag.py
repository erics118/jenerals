def mouseDrag(app, mouseX, mouseY):
    """Handle mouse drags"""

    if app.hasOngoingGame:
        inGameMouseDrag(app, mouseX, mouseY)
    else:
        startScreenMouseDrag(app, mouseX, mouseY)


def startScreenMouseDrag(app, mouseX, mouseY):
    """Handle mouse drags on the start screen"""

    pass


def inGameMouseDrag(app, mouseX, mouseY):
    """Handle mouse drags in the game"""

    if app.mouseCoords != None:
        app.isDragging = True
        app.board.left = mouseX - app.mouseCoords[0] + app.board.left
        app.board.top = mouseY - app.mouseCoords[1] + app.board.top
        app.mouseCoords = (mouseX, mouseY)
