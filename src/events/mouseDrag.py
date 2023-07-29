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

    app.isDragging = True
    app.board.left = mouseX - app.mx + app.board.left
    app.board.top = mouseY - app.my + app.board.top
    app.mx, app.my = mouseX, mouseY
