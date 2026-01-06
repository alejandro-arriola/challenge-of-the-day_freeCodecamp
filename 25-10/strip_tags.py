import re

def strip_tags(html):
    return re.sub(r"</?[^>]+>", "", html)

print(strip_tags('<a href="#">Click here</a>'))