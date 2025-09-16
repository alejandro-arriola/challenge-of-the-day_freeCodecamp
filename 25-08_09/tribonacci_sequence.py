def tribonacci_sequence(start_sequence, length):
    if length == 0:
        return []
    
    if length <= 3:
        return start_sequence[:length]
    
    trib = start_sequence

    for n in range(length-3):
        trib.append(start_sequence[-3] + start_sequence[-2] + start_sequence[-1])

    return trib

print(tribonacci_sequence([0, 0, 1], 20))