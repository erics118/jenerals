def floodFill(grid, coords=None):
    """
    Flood fill algorithm to find all the accessible areas in the grid.
    0 = unvisited
    1 = wall
    2 = visited
    """

    # having coords as None is the initial call
    # find the first non-wall cell and start the flood fill from there

    if coords is None:
        firstNotWall = next(
            (r, c)
            for r, row in enumerate(grid)
            for c, cell in enumerate(row)
            if cell == 0
        )

        floodFill(grid, firstNotWall)
        return

    # otherwise, actually do the flood fill
    r, c = coords

    # check out of bounds
    if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 0):
        return

    # if it is a wall, continue
    if grid[r][c] == 1:
        return

    # mark cell as visited
    grid[r][c] = 2

    # for each direction, flood fill from there
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Recursively move in all directions
    for dr, dc in directions:
        floodFill(grid, (r + dr, c + dc))


def hasInaccessibleAreas(grid):
    """
    Returns whether or not there are inaccessible areas in the grid.
    """

    return any(cell == 0 for row in grid for cell in row)
