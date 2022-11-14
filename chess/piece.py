from chess.color import Color
from chess.coordinates import Coordinates

class Piece:
    PIECE_NAMES = ['R', 'N', 'B', 'Q', 'K', 'P']

    def __init__(self, name, color, row, col):
        if name not in Piece.PIECE_NAMES:
            raise ValueError(f"Invalid piece name '{name}'")
        self.name = name
        self.color = Color(color) 
        self.coordinates = Coordinates(row, col)

    def __repr__(self):
        return self.color + self.name

