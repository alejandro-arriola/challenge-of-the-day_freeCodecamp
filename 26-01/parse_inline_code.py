import re

def parse_inline_code(markdown):
    return re.sub(r"`(.*?)`", lambda m: f"<code>{m.group(1)}</code>", markdown)