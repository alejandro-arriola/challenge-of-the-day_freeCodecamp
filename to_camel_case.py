import re

def to_camel_case(s):
    s = re.split("[\-_ ]+", s)
    s = [word.capitalize() for word in s]
    s[0] = s[0].lower()
    
    return ''.join(s)

print(to_camel_case("hello world"))