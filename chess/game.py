from chess.board import Board

class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        if player1.color == 'W':
            self.turn = 0
        else:
            self.turn = 1
        for player in self.players:
            for piece in player.pieces:
                self.board.board[piece.row][piece.col] = piece #TODO: board.board is bad design

    def move(self, piece, row, col):
        player = self.players[self.turn]
        #TODO: check that piece belongs to player
        self.board.board[piece.row][piece.col] = '-'
        self.board.board[row][col] = piece
        piece.row, piece.col = row, col
        #TODO: check that move is valid?

