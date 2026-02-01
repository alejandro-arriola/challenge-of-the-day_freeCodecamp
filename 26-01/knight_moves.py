def knight_moves(position):
    pos = ( 8 - int(position[1]), ord(position[0]) - 65 )
    moves = [ (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, -1), (2, 1), (-1, -2), (1, -2)]
    count = 0

    for move in moves:
        if move[0] + pos[0] >= 0 and move[0] + pos[0] < 8 and move[1] + pos[1] >= 0 and move[1] + pos[1] < 8:
            count += 1

    return count

print(knight_moves("G6"))