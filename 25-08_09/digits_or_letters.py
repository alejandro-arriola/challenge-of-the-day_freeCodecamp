from functools import reduce

def digits_or_letters(s):
    n_letters = reduce(lambda acc, char: acc + 1 if char.isalpha() else acc, s, 0)
    n_digits = reduce(lambda acc, char: acc + 1 if char.isdigit() else acc, s, 0)

    return "letters" if n_letters > n_digits else "digits" if n_digits > n_letters else "tie"


print(digits_or_letters("a1b2c3d"))



