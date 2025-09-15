** start of main.py **

def find_target(arr, target):
    indexes = []

    for i in range(len(arr)):
        for sub_i in range(i + 1, len(arr)):
            diff = target - arr[i]
            if arr[sub_i] == diff:
                return [ i, sub_i ]

    return "Target not found"

print(find_target([3, 2, 4, 5], 6))

** end of main.py **

