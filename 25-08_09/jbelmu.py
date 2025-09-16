def jbelmu(text):
    text = text.split()

    for i in range(len(text)):
        if len(text[i]) > 2:
            text[i] = text[i][0] + ''.join(sorted(text[i][1:-1])) + text[i][-1]

    return ' '.join(text)

print(jbelmu("freecodecamp is my favorite place to learn to code"))