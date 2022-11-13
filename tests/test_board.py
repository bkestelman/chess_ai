from chess.board import Board

def test_board_dimensions():
    board = Board()
    assert len(board.board) == 8
    for row in board.board:
        assert len(row) == 8

