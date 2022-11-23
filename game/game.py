"""
Abstract class representing arbitrary Games.

A Game is defined by its states, moves, and rules.

To create a Game, we need to specify the representation of its states and 
moves, as well as the rules by which we determine whether a given move is 
legal in the given state.
"""
from abc import ABC, abstractmethod # Abstract Base Class
import numpy as np

class Game(ABC):
    def __init__(self, state_shape, move_shape):
        self.state_shape = state_shape
        self.move_shape = move_shape
        self.state = np.zeros(self.state_shape)
        self.player = 0
        self.opponent = 1

    @abstractmethod
    def is_legal(self, move):
        pass

    """Make a move by updating state, if the move is legal"""
    @abstractmethod
    def make_move(self, move):
        pass

    @abstractmethod
    def legal_moves(self):
        pass

