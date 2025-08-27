from .board_operations import *

def get_pawn_sp_moves(source_field, board, piece_color, last_move):
    if not last_move:
        return {}
    source_id = field_index(source_field)
    pawn = board[source_id]
    vector = -1 if piece_color == 'w' else 1
    last_move_from, last_move_to = last_move

    sp_moves = {}
    for i in (-1, 1):
        if abs(source_id%8 - (source_id+i)%8) == 1:
            nbr = board[source_id+i]
            if field_index(last_move_to) == source_id+i:
                if are_same_type(pawn, nbr) and are_enemies(pawn, nbr) and last_move_from[0] == last_move_to[0]:
                    attack_field = source_id + 8*vector + i
                    sp_moves[f'{field_from_index(attack_field)}'] = 'enpassant'
    return sp_moves
    

def get_king_sp_moves(source_field, board, piece_color, last_move):
    pass

def get_pawn_moves(source_field, board, piece_color):
    source_id = field_index(source_field)
    row = int(source_field[1])
    moves = []

    vector = -1 if piece_color == 'w' else 1
    start_row = 2 if piece_color == 'w' else 7
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