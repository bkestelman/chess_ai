class State:
    def __init__(self):
        self.feature_planes = [None, None, None]
        WHITE = 0, BLACK = 1, MISC = 2
        self.feature_planes[WHITE] = {
                'P': init_pawns(),
                'R': init_rooks(),
                'N': init_knights(),
                'B': init_bishops(),
                'Q': init_queen(),
                'K': init_king(),
                'castling_allowed': np.ones(1),
                }
        self.feature_planes[BLACK] = {
                'P': init_pawns(),
                'R': init_rooks(),
                'N': init_knights(),
                'B': init_bishops(),
                'Q': init_queen(),
                'K': init_king(),
                'castling_allowed': np.ones(1)
                }
        self.feature_planes[MISC] = {
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

def init_knights():
    knights = empty_board()
    knights[0,1] = 1
    knights[0,6] = 1

def init_bishops():
    knights = empty_board()
    knights[0,2] = 1
    knights[0,5] = 1

def init_queen():
    knights = empty_board()
    knights[0,3] = 1

def init_king():
    knights = empty_board()
    knights[0,4] = 1

def empty_board():
    return np.zeros(8,8)

