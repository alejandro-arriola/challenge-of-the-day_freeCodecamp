def mask(card):
    sep = card[4]
    mask = "****"

    return (mask + sep) * 3 + card[-4:]

print(mask("4012-8888-8888-1881"))