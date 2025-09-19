def start_pose_fen():
    return 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'

# in the following code "piece" refers to 1-letter string such as 'r', 'R', 'Q' etc. or 'x' for empty field

def color_of(piece): 
    return 'x' if piece == 'x' else 'b' if piece.islower() else 'w'

def opp_color(color):
    return 'w' if color == 'b' else 'b' if color == 'w' else 'x'

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

def disable_castles_for_piece(piece_id, game): # changes castling attributes in game to False when it becomes unavailable
    piece = game.board[piece_id]
    if piece.lower() != 'k' and piece.lower() != 'r': # exit faster when piece can't castle anyway
        return None
    color = color_of(piece)
    castles = {
        ('k', 'w'): ['castle_lw', 'castle_sw'],
        ('k', 'b'): ['castle_lb', 'castle_sb'],
        ('r', 'w', 0): ['castle_lw'],
        ('r', 'w', 1): ['castle_sw'],
        ('r', 'b', 0): ['castle_lb'],
        ('r', 'b', 1): ['castle_sb'],
    }

    key = (piece.lower(), color)
    if piece.lower() == 'r':
        key = (piece.lower(), color, 0 if piece_id % 8 == 0 else 1)

    for attr in castles.get(key, []):
        setattr(game, attr, False)
    return None
        
        