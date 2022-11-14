class Coordinates:
    def __init__(self, row, col):
        if row < 0 or row > 7 or col < 0 or col > 7:
            raise ValueError(f'Board coordinates ({row}, {col}) out of range')
        self.row = row
        self.col = col

