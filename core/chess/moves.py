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
    # enpassant detection
    for i in (-1, 1): 
        nbr_id = source_id + i
        if abs(source_id%8 - (nbr_id)%8) == 1: # protection from going "a -> h" and "h -> a" file
            nbr = board[nbr_id]
            if last_move_to == nbr_id:
                attack_field = nbr_id + 8*vector
                if are_same_type(pawn, nbr) and are_enemies(pawn, nbr) and abs(last_move_from - (nbr_id)) == 16:
                    sp_moves[field_from_index(attack_field)] = 'enpassant'
    return sp_moves
    

def get_king_sp_moves(source_field, board, piece_color, last_move):
    return {}

def get_pawn_moves(source_field, board, piece_color):
    source_id = index_from_field(source_field)
    pawn = board[source_id]
    row = int(source_field[1])
    moves = []

    vector = -1 if piece_color == 'w' else 1
    start_row = 2 if piece_color == 'w' else 7
    if source_id > 7 and source_id < 56:
        if board[source_id + 8*vector] == 'x':
            moves.append(source_id + 8*vector) # standard move by 1 square
        for i in (-1, 1):
            target_id = source_id + 8*vector + i
            target = board[target_id]
            if are_enemies(pawn, target):
                moves.append(target_id) # move diagonally when taking
    if row == start_row: 
        moves.append(source_id + 16*vector) # first move by 2 squares
    return moves

def get_knight_moves(source_field, board, piece_color):
    moves = []
    source_id = index_from_field(source_field)
    knight = board[source_id]

    target_ids = [id for i in (-2, 2) for j in (-1, 1) for id in (source_id+8*i+j, source_id+8*j+i)]
    for id in target_ids:
        if abs(id%8 - source_id%8) > 2: # protection from going "a -> h" and etc.
                continue
        if id >= 0 and id < 64 and not are_friends(knight, board[id]):
            moves.append(id)
    return moves

def get_bishop_moves(source_field, board, piece_color):
    moves = []
    return moves

def get_rook_moves(source_field, board, piece_color):
    moves = []
    return moves

def get_queen_moves(source_field, board, piece_color):
    moves = []
    return moves

def get_king_moves(source_field, board, piece_color):
    moves = []
    source_id = index_from_field(source_field)
    king = board[source_id]
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            target_id = source_id + i*8 +j
            if abs(target_id%8 - source_id%8) > 1: # protection from going "a -> h" and "h -> a" file
                continue
            if target_id >= 0 and target_id < 64 and not are_friends(king, board[target_id]):
                moves.append(target_id) # standard moves by 1 square
    return moves