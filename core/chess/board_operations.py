def start_pose_fen():
    return 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'

# in the following code "piece" refers to 1-letter string such as 'r', 'R', 'Q' etc.

def color_of(piece): 
    return 'x' if piece == 'x' else 'b' if piece.islower() else 'w'

def are_enemies(piece1, piece2):
    return False if (piece1 == 'x' or piece2 == 'x') else color_of(piece1) != color_of(piece2)

def are_friends(piece1, piece2):
    return False if (piece1 == 'x' or piece2 == 'x') else color_of(piece1) == color_of(piece2)

def are_same_type(piece1, piece2):
    return piece1.lower() == piece2.lower()

def index_from_field(field): # return index of a field in 64bit board (e.g. 'a8' gives 0, 'g1' gives 62)
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