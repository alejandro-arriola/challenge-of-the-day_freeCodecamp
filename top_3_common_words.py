** start of main.py **

import re
from collections import Counter

def get_words(paragraph):
    paragraph  = re.split(r"[()\s.,!?]+", paragraph)
    paragraph = [word.lower() for word in paragraph]
    paragraph = Counter(paragraph)
    paragraph = paragraph.most_common(3)
    paragraph = [word for word, _ in paragraph]

    return paragraph

print(get_words("Wonder woman. is a woman"))

** end of main.py **

