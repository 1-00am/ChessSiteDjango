from .board_operations import field_index

def get_pawn_moves(source_field, board, piece_color):
    source_id = field_index(source_field)
    row = int(source_field[1])
    moves = []
    vector = 1 if piece_color == "b" else -1
    start_row = 2 if piece_color == "w" else 7
    if source_id < 56:
        moves.append(source_id + 8*vector)
    if row == start_row:
        moves.append(source_id + 16*vector)
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