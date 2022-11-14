from chess.piece import Piece

class Player:
    def __init__(self, color, first_row):
        if first_row != 0 and first_row != 7:
            raise ValueError(f"Invalid first row '{first_row}'")
        self.first_row = first_row
        if first_row == 0:
            second_row = 1
        elif first_row == 7:
            second_row = 6
        self.pieces = [
                Piece('R', color, first_row, 0),
                Piece('N', color, first_row, 1),
                Piece('B', color, first_row, 2),
                Piece('Q', color, first_row, 3),
                Piece('K', color, first_row, 4),
                Piece('B', color, first_row, 5),
                Piece('N', color, first_row, 6),
                Piece('R', color, first_row, 7),
                Piece('P', color, second_row, 0),
                Piece('P', color, second_row, 1),
                Piece('P', color, second_row, 2),
                Piece('P', color, second_row, 3),
                Piece('P', color, second_row, 4),
                Piece('P', color, second_row, 5),
                Piece('P', color, second_row, 6),
                Piece('P', color, second_row, 7),
                ]

