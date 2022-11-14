import pytest
from chess.piece import Piece

def test_coordinates_out_of_range():
    name = 'R'
    color = 'W'
    with pytest.raises(ValueError):
        piece = Piece(name, color, -1, 5)
    with pytest.raises(ValueError):
        piece = Piece(name, color, 5, -1)
    with pytest.raises(ValueError):
        piece = Piece(name, color, 8, 5)
    with pytest.raises(ValueError):
        piece = Piece(name, color, 5, 8)

def test_invalid_color():
    with pytest.raises(ValueError):
        piece = Piece('R', 'invalid color', 0, 0)

def test_invalid_piece_name():
    color = 'W'
    with pytest.raises(ValueError):
        piece = Piece('invalid name', color, 0, 0)

