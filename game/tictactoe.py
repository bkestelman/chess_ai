"""
Tic Tac Toe implementation of Game
"""
from game.game import Game
import numpy as np

class TicTacToe(Game):
    """
    state is represented as two 3x3 boards - one for each player
        This lets us represent both X and O with the same value of 1, which
        is convenient for machine learning.
        If we just used a single 3x3 board for both players, we would have
        to represent X as 1 and O as 2 (or somehow distinguish their values),
        which imputes an artificial ranking between the players, in this
        case making O's more important than X's
    
    move is represented as [row, col]
    """
    def __init__(self):
        super().__init__(state_shape=(2,3,3), move_shape=(2,))

    def is_legal(self, move):
        # any empty square is legal
        if move.shape != self.move_shape:
            raise InvalidMoveRepresentation()
        if move[0] < 0 or move[0] > self.state_shape[0]:
            raise MoveOutOfBounds()
        if move[1] < 0 or move[1] > self.state_shape[1]:
            raise MoveOutOfBounds()
        if (
                self.state[self.player, move[0], move[1]] != 0 and
                self.state[self.opponent, move[0], move[1]] != 0
        ):
            return False
        return True

    def make_move(self, move):
        if not self.is_legal(move):
            raise IllegalMove()
        self.state[self.player, move[0], move[1]] = 1
        self.player, self.opponent = self.opponent, self.player

    def legal_moves(self, move):
        raise NotImplemented()

    def is_game_over(self):
        return (
            np.any(self.state[self.player].sum(axis=0) == 3) or
            np.any(self.state[self.player].sum(axis=1) == 3) or
            self.state[self.player].trace() == 3 or
            np.fliplr(self.state[self.player]).trace() == 3 
            )

class InvalidMoveRepresentation(Exception):
    pass

class MoveOutOfBounds(Exception):
    pass

class IllegalMove(Exception):
    pass

