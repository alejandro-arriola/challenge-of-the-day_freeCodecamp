** start of main.py **

def is_valid_number(n, base):
    n = str(n).lower()

    chars = [b for b in range(0, base)]
    chars = list(map(lambda n: str(n) if n < 10 else chr(n - 10 + ord('a')), chars))
    chars = ''.join(chars)

    for digit in n:
        if not str(digit) in chars:
            return False

    return True

print(is_valid_number(2, 2))

** end of main.py **

