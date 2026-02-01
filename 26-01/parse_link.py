import re

def parse_link(markdown: str) -> str:
    m = re.match(r"\[(.*?)\]\((.*?)\)", markdown)
    text, url = m.groups()
    return f'<a href="{url}">{text}</a>'

print(parse_link("[freeCodeCamp](https://freecodecamp.org/)"))
