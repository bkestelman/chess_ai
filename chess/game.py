from chess.board import Board

class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        for player in self.players:
            for piece in player.pieces:
                self.board.board[piece.row][piece.col] = piece #TODO: board.board is bad design

