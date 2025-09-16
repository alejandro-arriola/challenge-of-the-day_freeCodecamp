import re

def is_pangram(sentence, letters):
    sentence = sentence.lower()
    sentence = re.sub(r'[^A-Za-z]', '', sentence)
    sentence = set(sentence)
    sentence = sorted(list(sentence))
    letters = sorted(list(letters))

    return sentence == letters

print(is_pangram("hello", "helo"))