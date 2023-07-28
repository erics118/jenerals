def isMoveLegal(app, cell, drow, dcol):
    newRow = cell[0] + drow
    newCol = cell[1] + dcol
    if not (0 <= newRow < app.board.rows):
        return

    if not (0 <= newCol < app.board.cols):
        return False

    if app.board.at(*cell).team != "player":
        return True

    if (
        app.board.at(newRow, newCol).isVisible
        and app.board.at(newRow, newCol).t == "mountain"
    ):
        return False

    return True
