def mouseDrag(app, mouseX, mouseY):
    app.board.left = mouseX - app.mx + app.board.left
    app.board.top = mouseY - app.my + app.board.top
    app.mx, app.my = mouseX, mouseY
