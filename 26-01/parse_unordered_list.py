import re

def parse_unordered_list(markdown):
    result = "<ul>" + re.sub(r"-\s+", "<li>", markdown)
    result = re.sub(r"\n", "</li>", result)

    return result + "</li></ul>"

print(parse_unordered_list("- A-1\n- A-2\n- B-1"))