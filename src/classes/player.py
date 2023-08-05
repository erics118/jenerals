class Player:
    """Player class"""

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.premoves = []
        self.isFocused = True
        self.premoveSelectedCoords = None
        self.selectedCoords = None
