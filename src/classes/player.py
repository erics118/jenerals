class Player:
    """Player class"""

    def __init__(self, playerId, name, color):
        self.playerId = playerId
        self.name = name
        self.color = color
        self.premoves = []
        self.isFocused = True
        self.premoveSelectedCoords = None
        self.selectedCoords = None
        self.generalCoords = None
