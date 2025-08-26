

def field_index(field):
    row = int(field[1])
    col = ord(field[0]) - 97
    return 8*(8-row) + col

print(field_index("h1"))
