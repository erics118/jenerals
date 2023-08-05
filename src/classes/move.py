class Move:
    """A class to represent a move."""

    def __init__(self, coords, moveTroops=True):
        self.coords = coords
        self.moveTroops = moveTroops

    def __iter__(self):
        return iter((self.coords, self.moveTroops))
