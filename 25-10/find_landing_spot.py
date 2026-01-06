def find_landing_spot(matrix):
    best_score = float('inf')
    best_coords = [-1, -1]

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == 0:
                score = 0

                if x - 1 >= 0:
                    score = score + matrix[y][x-1]
                if x + 1 < len(matrix[y]):
                    score = score + matrix[y][x+1]
                if y - 1 >= 0:
                    score = score + matrix[y-1][x]
                if y + 1 < len(matrix[y]):
                    score = score + matrix[y+1][x]

                if score <= best_score:
                    best_score = score
                    best_coords = [y, x]
    
    return best_coords

print(find_landing_spot([[9, 6, 0, 8], [7, 1, 1, 0], [3, 0, 3, 9], [8, 6, 0, 9]]))
