def flatten(arr):
    result = []

    def multiloop(arr):
        for item in arr:
            if isinstance(item, list):
                multiloop(item)
            else:
                result.append(item)
    
    multiloop(arr)

    return result

print(flatten([["L", "M", "N"], ["O", ["P", "Q", ["R", ["S", ["T", "U"]]]]], "V", ["W", ["X", ["Y", ["Z"]]]]]))