def find_duplicates(arr:int) -> list:
    duplicates = []
    seen = set()   
    
    for num in arr:
        if num in seen and num not in duplicates:
            duplicates.append(num)
        else:
            seen.add(num)

    return sorted(duplicates)

print(find_duplicates([2, 34, 0, 1, -6, 23, 5, 3, 2, 5, 67, -6, 23, 2, 43, 2, 12, 0, 2, 4, 4]))