class State:
    def __init__(self):
        self.feature_planes = [None, None, None]
        WHITE = 0, BLACK = 1, MISC = 2
        self.feature_planes[WHITE] = {
                'P': np.zeros(8, 8),
                'R': np.zeros(8, 8),
                'N': np.zeros(8, 8),
                'B': np.zeros(8, 8),
                'Q': np.zeros(8, 8),
                'K': np.zeros(8, 8),
                'castling_allowed': np.ones(1),
                }
        self.feature_planes[BLACK] = {
                'P': np.zeros(8, 8),
                'R': np.zeros(8, 8),
                'N': np.zeros(8, 8),
                'B': np.zeros(8, 8),
                'Q': np.zeros(8, 8),
                'K': np.zeros(8, 8),
                'castling_allowed': np.ones(1)
                }
        self.feature_planes[MISC] = {
                'repetitions': np.zeros(1), #TODO: how should these be represented?
                'moves_since_capture_or_pawn': np.zeros(1)
                }

