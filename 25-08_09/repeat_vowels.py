def repeat_vowels(s):
    repeater = 0
    s = list(s)

    for i in range(len(s)):
        if s[i] in "aeiouAEIOU":
            s[i] += s[i].lower() * repeater
            repeater += 1

    return "".join(s)

print(repeat_vowels("AEIOU"))