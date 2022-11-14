class Piece:
    PIECE_NAMES = ['R', 'N', 'B', 'Q', 'K', 'P']
    COLORS = ['W', 'B']

    def __init__(self, name, color, row, col):
        if name not in Piece.PIECE_NAMES:
            raise ValueError(f"Invalid piece name '{name}'")
        if color not in Piece.COLORS:
            raise ValueError(f"Invalid color '{color}'")
        if row < 0 or row > 7 or col < 0 or col > 7:
            raise ValueError(f"Piece position ({row}, {col}) out of range")
        self.name = name
        self.color = color 
        self.row = row
        self.col = col

    def __repr__(self):
        return self.color + self.name

