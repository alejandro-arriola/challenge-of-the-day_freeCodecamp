def decode(message, shift):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    shifted_lower = lower[shift:] + lower[:shift]
    shifted_upper = upper[shift:] + upper[:shift]
    print(shifted_lower, shifted_upper)
    # make translation table with both cases
    table = str.maketrans(shifted_lower + shifted_upper, lower + upper)
    
    return message.translate(table)

print(decode("Xlmw mw e wigvix qiwweki.", 4))

