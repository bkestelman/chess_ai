from chess.state import State
from chess.piece import Piece
import numpy as np

def test_initial_state():
    state = State()
    for piece in Piece.PIECE_NAMES:
        assert piece in state.feature_planes[state.WHITE]
        assert piece in state.feature_planes[state.BLACK]
    for color in [state.WHITE, state.BLACK]:
        feature_plane = state.feature_planes[color]
        assert np.all(feature_plane['P'][1,:] == 1)
        print(feature_plane['R'])
        assert feature_plane['R'][0,0] == 1
        assert feature_plane['R'][0,7] == 1
        assert feature_plane['N'][0,1] == 1
        assert feature_plane['N'][0,6] == 1
        assert feature_plane['B'][0,2] == 1
        assert feature_plane['B'][0,5] == 1
        assert feature_plane['Q'][0,3] == 1
        assert feature_plane['K'][0,4] == 1
        assert np.all(feature_plane['P'][2:,:] == 0)
        assert np.all(feature_plane['P'][0,:] == 0)
        assert np.all(feature_plane['R'][1:,:] == 0)
        assert np.all(feature_plane['N'][1:,:] == 0)
        assert np.all(feature_plane['B'][1:,:] == 0)
        assert np.all(feature_plane['Q'][1:,:] == 0)
        assert np.all(feature_plane['K'][1:,:] == 0)

