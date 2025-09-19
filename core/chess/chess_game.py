from .moves import *
from .board_operations import field_from_index, index_from_field, disable_castles_for_piece

def get_moves(source_field, board, piece, game): #returns moves as a list, and dict of special moves among them (e.g. 'enpassant')
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
    piece_type = piece[1] # piece is a 2-letter string where [0] is color and [1] is type (eg. wP, bQ)
    sp_moves = sp_moves_dict[piece_type](source_field, board, game) if piece_type in ('P', 'K') else {}
    moves = moves_dict[piece_type](source_field, board)
    moves = {field_from_index(m) for m in moves} | set(sp_moves.keys()) # using set to remove duplicates

    return list((moves)), sp_moves 

def make_move(source, target, game, special=None): # moves pieces across the board without registering
    source_id = index_from_field(source)
    target_id = index_from_field(target)
    board = game.board
    piece = board[source_id]
    color = color_of(piece)
    
    board = swap_piece(board[source_id], target_id, board)
    board = swap_piece('x', source_id, board)

    if special == 'enpassant':
        enemy_pawn_id = index_from_field(game.last_move_to)
        board = swap_piece('x', enemy_pawn_id, board)
    elif special == 'promotion':
        queen = 'Q' if color == 'w' else 'q'
        board = swap_piece(queen, target_id, board)
    elif special: # goes through when special is a castle variant
        coords = {
            'lb': 0, 'sb': 7,
            'lw': 56,'sw': 63   
        }
        vector = 1 if special[0] == 'l' else -1
        rook_id = coords[special]
        rook = board[rook_id]
        board = swap_piece(rook, target_id+vector, board)
        board = swap_piece('x', rook_id, board)

    disable_castles_for_piece(source_id, game) 
    disable_castles_for_piece(target_id, game)
    return board

def register_move(source, target, game, special=None): # registers move in game data
    board = make_move(source, target, game, special)
    game.last_move_from, game.last_move_to = source, target
    game.board = board
    game.save()

def get_player_moves(color, game):
    player_moves = [] # format of a move is (source, target)

    is_player_white = True if color == 'w' else False
    board = game.board
    for id in range(64):
        piece = board[id]
        if piece == 'x':
            continue
        if piece.isupper() == is_player_white: # checks if piece belongs to player
            moves, _ = get_moves(field_from_index(id), board, color+piece.upper(), game) # _ holds special moves, not used right now
            for move in moves:
                player_moves.append((field_from_index(id), move))

    return player_moves

def check_winner(board):
    pass