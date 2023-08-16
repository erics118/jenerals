def isMoveLegal(playerId, app, move):
    """
    Returns whether or not the move is legal.
    """

    isVisible = app.board.at(move.coords).isVisible or app.forceIsVisible

    # check bounds
    if (
        move.coords[0] < 0
        or move.coords[0] >= app.board.rows
        or move.coords[1] < 0
        or move.coords[1] >= app.board.cols
    ):
        return False

    # allow move if new cell is not visible
    if not isVisible:
        return True

    # allow all moves when not focused
    if not app.players[playerId].isFocused:
        return True

    # don't allow move if new cell is a mountain
    if isVisible and app.board.at(move.coords).t == "mountain":
        return False

    return True
