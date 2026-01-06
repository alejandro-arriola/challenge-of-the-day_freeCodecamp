import re

def check_strength(password):
    points = 0

    if re.compile(r"^.{8,}$").search(password):
        points = points + 1

    if re.compile(r"[a-z]").search(password) and re.compile(r"[A-Z]").search(password):
        points = points + 1
    
    if re.compile(r"\d").search(password):
        points = points + 1
    
    if re.compile(r"[!@#$%^&*]").search(password):
        points = points + 1

    return "weak" if points < 2 else "medium" if 2 <= points <= 3 else "strong" 

print(check_strength("PASSWORD"))