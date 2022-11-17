import numpy as np

class State:
    WHITE, BLACK, MISC = 0, 1, 2
    
    def __init__(self):
        self.feature_planes = [None, None, None]
        self.feature_planes[State.WHITE] = {
                'P': init_pawns(),
                'R': init_rooks(),
                'N': init_knights(),
                'B': init_bishops(),
                'Q': init_queen(),
                'K': init_king(),
                'castling_allowed': np.ones(1),
                }
        self.feature_planes[State.BLACK] = {
                'P': init_pawns(),
                'R': init_rooks(),
                'N': init_knights(),
                'B': init_bishops(),
                'Q': init_queen(),
                'K': init_king(),
                'castling_allowed': np.ones(1)
                }
        self.feature_planes[State.MISC] = {
                'repetitions': np.zeros(1), #TODO: how should these be represented?
                'moves_since_capture_or_pawn': np.zeros(1)
                }

def init_pawns():
    pawns = empty_board()
    pawns[1,:] = np.ones(8)
    return pawns

def init_rooks():
    rooks = empty_board()
    rooks[0,0] = 1
    rooks[0,7] = 1
    return rooks 

def init_knights():
    knights = empty_board()
    knights[0,1] = 1
    knights[0,6] = 1
    return knights 

def init_bishops():
    bishops = empty_board()
    bishops[0,2] = 1
    bishops[0,5] = 1
    return bishops 

def init_queen():
    queens = empty_board()
    queens[0,3] = 1
    return queens 

def init_king():
    kings = empty_board()
    kings[0,4] = 1
    return kings

def empty_board():
    return np.zeros((8,8))

