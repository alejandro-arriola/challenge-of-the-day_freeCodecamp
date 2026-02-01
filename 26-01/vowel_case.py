import re

def vowel_case(s):
    return re.sub(r"[aeiou]", lambda m: m.group(0).upper(), s.lower())

print(vowel_case("HELLO, world!"))