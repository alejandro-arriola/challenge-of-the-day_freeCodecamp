def is_balanced(s):
    first_half = s[0:len(s) // 2]
    second_half = s[(len(s)+1)//2:]

    return sum(1 for char in first_half if char.lower() in "aeiuo") == sum(1 for char in second_half if char.lower() in "aeiuo")

print(is_balanced("Wonder Woman is Lynda Carter."))

