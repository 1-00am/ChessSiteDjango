from .moves import *
from .board_operations import field_from_index

def get_moves(where_from, board, piece, last_move):
    moves_dict = {
        'P': get_pawn_moves,
        'N': get_knight_moves,
        'B': get_bishop_moves,
        'R': get_rook_moves,
        'Q': get_queen_moves,
        'K': get_king_moves
    }
    sp_moves_dict = {
        'P': get_pawn_sp_moves,
        'K': get_king_sp_moves
    }
    piece_color = piece[0] # piece is a 2-letter string where [0] is color and [1] is type
    piece_type = piece[1]

    sp_moves = sp_moves_dict[piece_type](where_from, board, piece_color, last_move) if piece_type in ('P', 'K') else {}
    moves = moves_dict[piece_type](where_from, board, piece_color)

    moves = [field_from_index(move) for move in moves.copy()]
    for move in sp_moves.keys():
        moves.append(move)

    return moves, sp_moves

def check_winner(board):
    pass