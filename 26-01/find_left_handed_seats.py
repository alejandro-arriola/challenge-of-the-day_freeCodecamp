def find_left_handed_seats(table):
    rowLen = len(table[0])
    sits = 0

    for i in range(rowLen - 1):
        if table[0][i] == "U" and table[0][i+1] != "R":
            sits += 1

        if table[1][rowLen-i-1] == "U" and table[1][rowLen-i-2] != "R":
            sits += 1

    if table[0][-1] == "U":
        sits += 1
    if table[1][0] == "U":
        sits += 1

    return sits

print(find_left_handed_seats([["U", "R", "U", "L"], ["U", "R", "R", "R"]]))