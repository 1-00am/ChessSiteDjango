
def get_pawn_moves(where_from, board, piece_color):
    moves = []
    vector = 1 if piece_color == "b" else -1
    if where_from < 56:
        moves.append(where_from + 8*vector)
    return moves

def get_knight_moves(where_from, board, piece_color):
    moves = []
    return moves

def get_bishop_moves(where_from, board, piece_color):
    moves = []
    return moves

def get_rook_moves(where_from, board, piece_color):
    moves = []
    return moves

def get_queen_moves(where_from, board, piece_color):
    moves = []
    return moves

def get_king_moves(where_from, board, piece_color):
    moves = []
    return moves