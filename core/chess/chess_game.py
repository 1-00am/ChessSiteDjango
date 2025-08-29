from .moves import *
from .board_operations import field_from_index, index_from_field

def get_moves(source, board, piece, last_move): #returns moves as an array, and dict of special moves among them (e.g. 'castle' 'enpassant')
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

    sp_moves = sp_moves_dict[piece_type](source, board, piece_color, last_move) if piece_type in ('P', 'K') else {}
    moves = moves_dict[piece_type](source, board, piece_color)

    moves = [field_from_index(move) for move in moves.copy()]
    for move in sp_moves.keys():
        moves.append(move)

    return moves, sp_moves

def make_move(source, target, game, special=None):
    source_id = index_from_field(source)
    target_id = index_from_field(target)
    board = game.board

    board = board[:target_id] + board[source_id] + board[target_id+1:]
    board = board[:source_id] + 'x' + board[source_id+1:]
    if special == 'enpassant':
        enemy_pawn_id = index_from_field(game.last_move_to)
        board = board[:enemy_pawn_id] + 'x' + board[enemy_pawn_id+1:]

    game.last_move_from, game.last_move_to = source, target
    game.board = board
    game.save()
    return None


def check_winner(board):
    pass