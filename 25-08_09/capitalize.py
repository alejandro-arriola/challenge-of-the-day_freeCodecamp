def capitalize(paragraph):
    paragraph = list(paragraph)
    capitalized = []
    sentence_chars = []

    for char in paragraph:
        if char.isalpha() or char in " ,'":
            sentence_chars.append(char)
        else:
            if sentence_chars != []:
                for sub_i in range(len(sentence_chars)):
                    if sentence_chars[sub_i].isalpha():
                        sentence_chars[sub_i] = sentence_chars[sub_i].upper()
                        break
                capitalized.extend(sentence_chars)
                sentence_chars.clear()
            capitalized.append(char)
            
    return "".join(capitalized)

print(capitalize("I did today's coding challenge... It was fun!!"))