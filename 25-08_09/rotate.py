def rotate(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

print(rotate([[1, 2], [3, 4]]))