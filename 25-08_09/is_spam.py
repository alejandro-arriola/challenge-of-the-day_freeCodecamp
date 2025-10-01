import re
from functools import reduce

def is_spam(number):
    number = re.sub(r'[+()]', '', number)
    number = re.split(r"[ -]", number)

    if len(number[0]) > 2 or number[0][0] != "0":
        return True

    if int(number[1]) > 900 or int(number[1]) < 200:
        return True
    
    ftd = reduce(lambda acc, n: acc + int(n), number[2], 0)
    if str(ftd) in number[3]:
        return True

    number = "".join(number)
    if re.search(r"(\d)\1{3,}", number):
        return True

    return False

print(is_spam("+0 (200) 234-0182"))