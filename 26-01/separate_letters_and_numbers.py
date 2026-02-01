import re

def separate_letters_and_numbers(s):
    s = re.sub(r"([a-zA-Z]+)([0-9]+)", r"\1-\2", s)
    return re.sub(r"([0-9]+)([a-zA-Z]+)", r"\1-\2", s)

print(separate_letters_and_numbers("ABC123"))