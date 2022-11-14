import pytest
from chess.coordinates import Coordinates
from chess.color import Color
from chess.piece import Piece

def test_coordinates_out_of_range():
    with pytest.raises(ValueError):
        cor = Coordinates(-1, 5)
    with pytest.raises(ValueError):
        cor = Coordinates(5, -1)
    with pytest.raises(ValueError):
        cor = Coordinates(8, 5)
    with pytest.raises(ValueError):
        cor = Coordinates(5, 8)

def test_invalid_color():
    with pytest.raises(ValueError):
        color = Color('invalid color')
    with pytest.raises(ValueError):
        piece = Piece('R', 'invalid color', 0, 0)

def test_invalid_piece_name():
    color = 'W'
    with pytest.raises(ValueError):
        piece = Piece('invalid name', color, 0, 0)

