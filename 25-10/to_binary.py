def to_binary(decimal):
    resp = ""

    while decimal >= 2:
        resp = resp + str(decimal % 2)
        decimal = decimal // 2

    resp = resp + str(decimal)
    
    return resp[::-1]

print(to_binary(5))