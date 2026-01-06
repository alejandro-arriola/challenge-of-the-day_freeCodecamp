def hex_to_decimal(hex):
    dec = 0
    hexas = { "A":10, "B":11,"C":12, "D":13, "E":14, "F":15 }

    for digit in hex:
        if digit.isdigit():
            dec = dec * 16 + int(digit)
        else:
            dec = dec * 16 + hexas[digit] 

    return dec

print(hex_to_decimal("A3F"))