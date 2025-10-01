def find_missing_numbers(arr):
    arr.sort()
    arr = set(arr)
    arr = list(arr)
    missing = []
    
    for n in range(1, arr[-1]+1):
        if not n in arr:
            missing.append(n)

    return missing

print(find_missing_numbers([3, 1, 4, 1, 5, 9]))