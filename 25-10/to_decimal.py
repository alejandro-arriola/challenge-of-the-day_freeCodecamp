def to_decimal(binary):
    binary = list(map(int, binary[::-1]))
    decimal = 0

    for e, d in enumerate(binary):
        decimal = decimal + (d * (2**e))

    return decimal

print(to_decimal("10010"))