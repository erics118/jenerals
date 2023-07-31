def isMoveLegal(app, cell, moveCoords):
    """
    Returns whether or not the move is legal.
    """

    newCoords = (cell[0] + moveCoords[0], cell[1] + moveCoords[1])

    # check bounds
    if not (0 <= newCoords[0] < app.board.rows and 0 <= newCoords[1] < app.board.cols):
        return False

    # allow move if new cell is not visible
    if not app.board.at(*newCoords).isVisible:
        return True

    # don't allow move if new cell is a mountain
    if app.board.at(*newCoords).isVisible and app.board.at(*newCoords).t == "mountain":
        return False

    return True
