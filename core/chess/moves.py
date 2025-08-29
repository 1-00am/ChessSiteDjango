from .board_operations import *

def get_pawn_sp_moves(source_field, board, piece_color, last_move):
    if not last_move:
        return {}
    source_id = index_from_field(source_field)
    pawn = board[source_id]
    vector = -1 if piece_color == 'w' else 1
    last_move_from = index_from_field(last_move[0])
    last_move_to = index_from_field(last_move[1])

    sp_moves = {}
    for i in (-1, 1):
        nbr_id = source_id + i
        if abs(source_id%8 - (nbr_id)%8) == 1: # protection from going "a -> h" and "h -> a" file
            nbr = board[nbr_id]
            if last_move_to == nbr_id:
                attack_field = nbr_id + 8*vector
                if are_same_type(pawn, nbr) and are_enemies(pawn, nbr) and abs(last_move_from - (nbr_id)) == 16:
                    sp_moves[f'{field_from_index(attack_field)}'] = 'enpassant'
    return sp_moves
    

def get_king_sp_moves(source_field, board, piece_color, last_move):
    pass

def get_pawn_moves(source_field, board, piece_color):
    source_id = index_from_field(source_field)
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