def start_pose_fen():
    return 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'

# in the following code "piece" refers to 1-letter string such as 'r', 'R', 'Q' etc. or 'x' for empty field

def color_of(piece): 
    return 'x' if piece == 'x' else 'b' if piece.islower() else 'w'

# def change_color_to(piece, color):
#     return piece.lower() if color == 'b' else piece.upper()

def are_enemies(piece1, piece2):
    return False if (piece1 == 'x' or piece2 == 'x') else color_of(piece1) != color_of(piece2)

def are_friends(piece1, piece2):
    return False if (piece1 == 'x' or piece2 == 'x') else color_of(piece1) == color_of(piece2)

def are_same_type(piece1, piece2):
    return piece1.lower() == piece2.lower()

def index_from_field(field): # return index of a field in 64-character board (e.g. 'a8' gives 0, 'g1' gives 62)
    row = int(field[1])
    col = ord(field[0]) - 97
    return 8*(8-row) + col

def field_from_index(id): # return a field in standard notation from given board index
    col_num = id%8
    col_let = chr(col_num+97) 
    row = str(8 - (id-col_num)//8)
    return col_let+row

def fen_to_64char(fen): # transforms short-fen into 64-character board
    brd = ''
    for i in range(len(fen)):
        if fen[i].isdigit():
            brd += 'x'*(int(fen[i]))
        elif fen[i] != '/':
            brd += fen[i]
    return brd

def swap_piece(piece, id, board):
    return board[:id] + piece + board[id+1:]

def disable_castles_for_piece(piece_id, game):
    board = game.board
    piece = board[piece_id]
    color = color_of(piece)
    if piece.lower() == 'k':
        if color == 'w':
            game.castle_lw = False
            game.castle_sw = False
        else:
            game.castle_lb = False
            game.castle_sb = False
    elif piece.lower() == 'r':
        if piece_id%8 == 0:
            if color == 'w':
                game.castle_lw = False
            else:
                game.castle_lb = False
        else:
            if color == 'w':
                game.castle_sw = False
            else:
                game.castle_sb = False
    return None
        
        