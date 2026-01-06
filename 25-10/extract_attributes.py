import re

def extract_attributes(element):
    pattern = r'\w+="[^"]*"'
    result = re.findall(pattern, element)

    if (not result): 
        return []

    result = [pair.replace('=', ', ').replace('"', '') for pair in result]

    return result

print(extract_attributes('<input name="email" type="email" required="true" />'))