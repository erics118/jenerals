def isMoveLegal(app, cell, drow, dcol):
    if not (0 <= cell[0] + drow < app.board.rows):
        return

    if not (0 <= cell[1] + dcol < app.board.cols):
        return False

    if app.board.at(cell[0] + drow, cell[1] + dcol).t == "mountain":
        return False

    return True
