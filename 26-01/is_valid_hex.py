import re

def is_valid_hex(s):
    return bool(re.match(r"^#(?:[0-9A-Fa-f]{3}|[0-9A-Fa-f]{6})$", s))

print(is_valid_hex("#123"))