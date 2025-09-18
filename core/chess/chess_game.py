from .moves import *
from .board_operations import field_from_index, index_from_field, disable_castles_for_piece

def get_moves(source_field, board, piece, game): #returns moves as an array, and dict of special moves among them (e.g. 'castle_lw' 'enpassant')
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
    piece_type = piece[1] # piece is a 2-letter string where [0] is color and [1] is type

    sp_moves = sp_moves_dict[piece_type](source_field, board, game) if piece_type in ('P', 'K') else {}
    moves = moves_dict[piece_type](source_field, board)

    moves = [field_from_index(move) for move in moves.copy()]
    for move in sp_moves.keys():
        moves.append(move)

    print(list(set(moves)), sp_moves)
    return list(set(moves)), sp_moves # removing duplicates from moves

def make_move(source, target, game, special=None):
    source_id = index_from_field(source)
    target_id = index_from_field(target)
    board = game.board
    piece = board[source_id]
    color = color_of(piece)
    board = game.board

    board = swap_piece(board[source_id], target_id, board)
    board = swap_piece('x', source_id, board)

    if special == 'enpassant':
        enemy_pawn_id = index_from_field(game.last_move_to)
        board = board[:enemy_pawn_id] + 'x' + board[enemy_pawn_id+1:]
    elif special == 'promotion':
        queen = 'Q' if color == 'w' else 'q'
        board = board[:target_id] + queen + board[target_id+1:]

    disable_castles_for_piece(source_id, game)
    #print('lw', game.castle_lw, 'sw', game.castle_sw, 'lb', game.castle_lb, 'sb', game.castle_sb)

    game.last_move_from, game.last_move_to = source, target
    game.board = board
    game.save()
    return None


def check_winner(board):
    pass

def get_player_moves(color, game):
    player_moves = [] # format of a move is (source, target)

    is_player_white = True if color == 'w' else False
    board = game.board
    for i in range(64):
        piece = board[i]
        if piece == 'x':
            continue
        if piece.isupper() == is_player_white: # checks if piece belongs to player
            moves, _ = get_moves(field_from_index(i), board, color+piece.upper(), game)
            for move in moves:
                player_moves.append((field_from_index(i), move))

    return player_moves