import re

def count(text, parameter):
    matches = re.findall(f"(?=({parameter}))", text)

    return len(matches)

print(count("aaa", "aa"))