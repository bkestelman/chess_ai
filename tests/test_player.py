import pytest
from chess.player import Player
from chess.color import Color

def test_player_constructor():
    first_row = 0
    for color in Color.COLORS:
        player = Player(color, first_row)
        assert len(player.pieces) == 16

def test_invalid_first_row():
    first_row = 5
    color = Color.COLORS[0]
    with pytest.raises(ValueError):
        player = Player(color, first_row)

