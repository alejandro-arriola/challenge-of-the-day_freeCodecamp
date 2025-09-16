def fibonacci_sequence(start_sequence, length):
    if length == 0:
        return []

    if length == 1:
        return [ start_sequence[0] ]
    
    if length == 2:
        return start_sequence
    
    for _ in range(2, length):
        start_sequence.append(start_sequence[-2] + start_sequence[-1])

    return start_sequence

print(fibonacci_sequence([0, 1], 20))