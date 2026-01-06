import re

def validate(email):
    pattern = re.compile(r'^(?!.*\.\.)[A-Za-z0-9_-](?:[A-Za-z0-9._-]*[A-Za-z0-9_-])?@[A-Za-z0-9!.-]+\.[A-Za-z]{2,}$')
    return bool(re.fullmatch(pattern, email))

print(validate("a@b.cd"))