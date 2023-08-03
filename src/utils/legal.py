def isCoordLegal(app, newCoords):
    """
    Returns whether or not the move is legal.
    """

    isVisible = app.board.at(newCoords).isVisible or app.forceIsVisible

    # check bounds
    if not (
        0 <= newCoords[0] < app.board.rows
        and 0 <= newCoords[1] < app.board.cols
    ):
        return False

    # allow move if new cell is not visible
    if not isVisible:
        return True

    # don't allow move if new cell is a mountain
    if isVisible and app.board.at(newCoords).t == "mountain":
        return False

    return True
