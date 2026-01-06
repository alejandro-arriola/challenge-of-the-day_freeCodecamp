def sock_pairs(pairs, cycles):
    pairs *= 2

    for c in range(1, cycles + 1):
        if c % 2 == 0:
            if pairs > 0:
                pairs -= 1
        if c % 3 == 0:
            pairs += 1
        if c % 5 == 0:
            if pairs > 0:
                pairs -= 1
        if c % 10 == 0:
            pairs += 2

    return pairs // 2

print(sock_pairs(2, 5)) #1
print(sock_pairs(5, 11)) #4
print(sock_pairs(6, 25)) #3