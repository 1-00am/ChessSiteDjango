from .moves import *

def start_pose_fen():
    return 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'

def curr_player():
    pass

def get_moves(where_from, board, piece):
    moves_dict = {
        'P': get_pawn_moves,
        'N': get_knight_moves,
        'B': get_bishop_moves,
        'R': get_rook_moves,
        'Q': get_queen_moves,
        'K': get_king_moves
    }
    piece_color = piece[0] # piece is a 2-letter string where [0] is color and [1] is type
    piece_type = piece[1]

    return moves_dict[piece_type](where_from, board, piece_color)

def check_winner(board):
    pass