def second_largest(arr):
    return sorted(list(set(arr)), reverse=True)[1]

print(second_largest([1, 0, -1, 0, 1, 0, -1, 1, 0]))


