# 0 = unvisited
# 1 = wall
# 2 = visited
def floodFill(grid, r=None, c=None):
    if r is None or c is None:
        firstNotWall = None
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    firstNotWall = (r, c)
                    break
        floodFill(grid, *firstNotWall)

    if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 0):
        return

    grid[r][c] = 2

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Recursively move in all directions
    for dr, dc in directions:
        floodFill(grid, r + dr, c + dc)


def hasInaccessibleAreas(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 0:
                return True
    return False
