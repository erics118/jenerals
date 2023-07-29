# 0 = unvisited
# 1 = wall
# 2 = visited
def floodFill(grid, coords=None):
    # having coords as None is the initial call
    # find the first non-wall cell and start the flood fill from there
    if coords == None:
        firstNotWall = None
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    firstNotWall = (r, c)
                    break

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
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 0:
                return True
    return False
