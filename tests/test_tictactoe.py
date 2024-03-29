from game.tictactoe import TicTacToe
from game.game import Game
import numpy as np

def test_new_game():
    tictactoe = TicTacToe()
    assert(tictactoe.state.shape == (2,3,3))
    assert(tictactoe.player is not None)
    assert(tictactoe.opponent is not None)

def test_move():
    tictactoe = TicTacToe()
    first_player = tictactoe.player
    second_player = tictactoe.opponent
    move = np.array([0, 0])
    tictactoe.make_move(move)
    assert(tictactoe.player == second_player)
    assert(tictactoe.opponent == first_player)
    assert(tictactoe.state[first_player, 0, 0] == 1)

def test_is_game_over():
    tictactoe = TicTacToe()
    first_player = tictactoe.player
    second_player = tictactoe.opponent
    assert(not tictactoe.did_win(first_player))
    assert(not tictactoe.did_win(second_player))
    tictactoe.state[first_player] = np.array([[1, 1, 1], [0, 0, 0], [0, 0, 0]])
    assert(tictactoe.did_win(first_player))
    tictactoe.state[first_player] = np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]])
    assert(tictactoe.did_win(first_player))
    tictactoe.state[first_player] = np.array([[0, 0, 0], [0, 0, 0], [1, 1, 1]])
    assert(tictactoe.did_win(first_player))
    tictactoe.state[first_player] = np.array([[1, 0, 0], [1, 0, 0], [1, 0, 0]])
    assert(tictactoe.did_win(first_player))
    tictactoe.state[first_player] = np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]])
    assert(tictactoe.did_win(first_player))
    tictactoe.state[first_player] = np.array([[0, 0, 1], [0, 0, 1], [0, 0, 1]])
    assert(tictactoe.did_win(first_player))
    tictactoe.state[first_player] = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    assert(tictactoe.did_win(first_player))
    tictactoe.state[first_player] = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    assert(tictactoe.did_win(first_player))

