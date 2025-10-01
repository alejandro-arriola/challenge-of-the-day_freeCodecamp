from functools import reduce

def is_mirror(str1, str2):
    str1 = reduce(lambda acc, char: acc + char if char.isalpha() else acc, str1, "")
    str2 = str2[::-1]
    str2 = reduce(lambda acc, char: acc + char if char.isalpha() else acc, str2, "")

    return str1 == str2


print(is_mirror("Hello World", "dlroW-olleH"))



