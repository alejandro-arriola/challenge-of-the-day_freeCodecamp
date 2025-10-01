import re
from functools import reduce

def get_longest_word(sentence):
    sentence = re.sub(r"[.]", "", sentence).split(" ")
    sentence = reduce(lambda longest, current: current if len(current) > len(longest) else longest, sentence, "")

    return sentence

print(get_longest_word("Coding challenges are fun and educational."))