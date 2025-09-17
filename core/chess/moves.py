from .board_operations import *

def get_pawn_sp_moves(source_field, board, last_move):
    if not last_move:
        return {}
    source_id = index_from_field(source_field)
    pawn = board[source_id]
    color = color_of(pawn)
    vector = -1 if color == 'w' else 1
    last_move_from = index_from_field(last_move[0])
    last_move_to = index_from_field(last_move[1])

    sp_moves = {}
    # enpassant detection
    for i in (-1, 1): 
        nbr_id = source_id + i
        if abs(source_id%8 - (nbr_id)%8) != 1: # protection from going "a -> h" and "h -> a" file
            continue 
        nbr = board[nbr_id]
        if last_move_to == nbr_id:
            target_id = nbr_id + 8*vector
            if are_same_type(pawn, nbr) and are_enemies(pawn, nbr) and abs(last_move_from - (nbr_id)) == 16:
                sp_moves[field_from_index(target_id)] = 'enpassant'
    # promotion (only queen now)
    promo_row = 1 if color == 'w' else 6  
    if source_id // 8 == promo_row:
        for i in (-1, 1):
            target_id = source_id + 8*vector + i
            if target_id < 0 or target_id > 63:
                continue
            target = board[target_id]
            if abs(source_id%8 - (target_id)%8) != 1:
                continue
            if not are_friends(pawn, target):
                sp_moves[field_from_index(target_id)] = 'promotion'
        target_id = source_id + 8*vector
        if board[target_id] == 'x':
            sp_moves[field_from_index(target_id)] = 'promotion'
    return sp_moves
    
def get_king_sp_moves(source_field, board, last_move):
    
    return {}

def get_pawn_moves(source_field, board):
    source_id = index_from_field(source_field)
    pawn = board[source_id]
    color = color_of(pawn)
    row = int(source_field[1])
    moves = []

    vector = -1 if color == 'w' else 1
    start_row = 2 if color == 'w' else 7
    if source_id > 7 and source_id < 56:
        if board[source_id + 8*vector] == 'x':
            moves.append(source_id + 8*vector) # standard move by 1 square
        for i in (-1, 1):
            target_id = source_id + 8*vector + i
            if abs(target_id%8 - source_id%8) > 1: # protection from going "a -> h" and etc.
                continue
            target = board[target_id]
            if are_enemies(pawn, target):
                moves.append(target_id) # move diagonally when taking
    if row == start_row and board[source_id+8*vector] == 'x' and board[source_id+16*vector] == 'x': 
        moves.append(source_id + 16*vector) # first move by 2 squares
    return moves

def get_knight_moves(source_field, board):
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

def move_search_in_directions(source_field, board, directions): # similiar code for bishop and rook made into a function
    moves = []
    source_id = index_from_field(source_field)
    myself = board[source_id]
    for dire in directions:
        target_id = source_id
        while True:
            target_id += 8*dire[0] + dire[1]
            if target_id < 0 or target_id > 63 or are_friends(myself, board[target_id]):
                break
            elif abs(target_id%8 - (target_id-dire[1])%8) > 1: # break if looped over rows during vertical moves search 
                break
            elif are_enemies(myself, board[target_id]):
                moves.append(target_id) # break after adding enemy piece as move
                break
            else:
                moves.append(target_id) # add empty field
    return moves

def get_bishop_moves(source_field, board):
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    return move_search_in_directions(source_field, board, directions)

def get_rook_moves(source_field, board):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    return move_search_in_directions(source_field, board, directions)
    
def get_queen_moves(source_field, board):
    return get_rook_moves(source_field, board) + get_bishop_moves(source_field, board)

def get_king_moves(source_field, board):
    moves = []
    source_id = index_from_field(source_field)
    king = board[source_id]
    target_ids = [source_id+8*i+j for i in (-1, 0, 1) for j in (-1, 0, 1)]
    for id in target_ids:
        if abs(id%8 - source_id%8) > 1: # protection from going "a -> h" and "h -> a" file
            continue
        if id >= 0 and id < 64 and not are_friends(king, board[id]):
                moves.append(id) # standard moves by 1 square
    return moves