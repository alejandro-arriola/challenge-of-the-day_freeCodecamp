def parse_roman_numeral(numeral):
    numeral = list(numeral)
    numeral = numeral[::-1]

    for i in range(len(numeral)):
        match numeral[i]:
            case 'M':
                numeral[i] = 1000
            case 'D':
                numeral[i] = 500
            case 'C':
                numeral[i] = 100
            case 'L':
                numeral[i] = 50
            case 'X':
                numeral[i] = 10
            case 'V':
                numeral[i] = 5
            case _:
                numeral[i] = 1
        
        if i != 0:
            if numeral[i-1] > numeral[i]:
                numeral[i] = -numeral[i]

    return sum(numeral)

print(parse_roman_numeral("XCIX"))