def is_sorted(arr):
    if arr == sorted(arr):
        return "Ascending"
    
    if arr == sorted(arr, reverse=True):
        return "Descending"

    return "Not sorted"

print(is_sorted([1, 2, 3, 4, 5]))