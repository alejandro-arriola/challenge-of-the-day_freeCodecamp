def array_diff(arr1, arr2):
    arr1.extend(arr2)

    for word in arr1:
        if arr1.count(word) == 2:
            arr1.remove(word)
            arr1.remove(word)

    return arr1

print(array_diff(["I", "like", "freeCodeCamp"], ["I", "like", "rocks"]))