def boundedMove(app, cell, drow, dcol):
    newRow = min(max(cell[0] + drow, 0), app.rows - 1)
    newCol = min(max(cell[1] + dcol, 0), app.cols - 1)
    return (newRow, newCol)


def keyPress(app, key):
    if key == "space":
        app.isFocused = not app.isFocused
    elif key == "left":
        app.selectedCell = boundedMove(app, app.selectedCell, 0, -1)
    elif key == "right":
        app.selectedCell = boundedMove(app, app.selectedCell, 0, 1)
    elif key == "up":
        app.selectedCell = boundedMove(app, app.selectedCell, -1, 0)
    elif key == "down":
        app.selectedCell = boundedMove(app, app.selectedCell, 1, 0)


# TODO: key hold
