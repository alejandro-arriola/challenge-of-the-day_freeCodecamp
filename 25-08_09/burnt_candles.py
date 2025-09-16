def burn_candles(candles, leftovers_needed):
    burnt = 0
    leftovers = 0

    while True:
        burnt += candles
        leftovers += candles

        candles = leftovers // leftovers_needed
        leftovers -= candles * leftovers_needed

        if candles == 0:
            break

    return burnt

print(burn_candles(7, 2))

