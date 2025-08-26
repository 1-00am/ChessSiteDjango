from .moves import *
import string

def start_pose_fen():
    return 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'

def field_index(field): # return index of a field in 64bit board (eg. 'a8' gives 0, 'g1' gives 62)
    row = int(field[1])
    col = ord(field[0]) - 97
    return 8*(8-row) + col

def field_from_index(id): # return a field in standard notation from given board index
    col_num = id%8
    col_let = chr(col_num+97) 
    row = str(8 - (id-col_num)//8)
    return col_let+row

def fen_to_64bit(fen): # transforms short-fen into 64bit board
    brd = ''
    for i in range(len(fen)):
        if fen[i].isdigit():
            brd += 'x'*(int(fen[i]))
        elif fen[i] != '/':
            brd += fen[i]
    return brd

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
    where_from = field_index(where_from)

    moves = moves_dict[piece_type](where_from, board, piece_color)
    return [field_from_index(move) for move in moves]

def check_winner(board):
    pass