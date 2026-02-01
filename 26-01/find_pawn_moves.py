def find_pawn_moves(position):
    return [ position[0] + "3", position[0] + "4" ] if position [1] == "2" else [ position[0] + str(int(position[1]) + 1) ]

print(find_pawn_moves("G2"))