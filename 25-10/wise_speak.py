def wise_speak(sentence):
    words = [ "have", "must", "are", "will", "can" ]

    for word in words:
        pos = sentence.find(word)
        if pos != -1:
            break
    
    if pos == -1:
        return "ERROR: bad egg"
    
    result = sentence[pos+len(word)+1:-1]
    result = result.capitalize() + ", "
    result = result + sentence[:pos+len(word)].lower() + sentence[-1]

    return result

print(wise_speak("Do you think you will complete this?"))