import re

def to_consonant_case(s):
    s = re.sub(r"[bcdfghjklmnpqrstvwxyz]", 
               lambda m: m.group().upper(), 
               s, 
               flags=re.IGNORECASE)

    s = re.sub(r"[aeiou]", 
               lambda m: m.group().lower(), 
               s, 
               flags=re.IGNORECASE)

    return s.replace("-", "_")