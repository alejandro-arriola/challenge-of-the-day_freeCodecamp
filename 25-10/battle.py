import math

def battle(our_team, opponent):
    our_team = our_team.split(" ")
    our_team = list(map(lambda word: list(word), our_team))
    opponent = opponent.split(" ")
    opponent = list(map(lambda word: list(word), opponent))
    W = 0
    L = 0

    for our_word, ur_word in zip(our_team, opponent):
        our_word = sum(list(map(lambda char: ord(char) - ord('a') + 1 if 'a' <= char <= 'z' else (ord(char) - ord('A') + 1) * 2, our_word)))
        ur_word = sum(list(map(lambda char: ord(char) - ord('a') + 1 if 'a' <= char <= 'z' else (ord(char) - ord('A') + 1) * 2, ur_word)))
        if our_word > ur_word:
            W = W + 1
        elif ur_word > our_word:
            L = L + 1

    return "We win" if W > L else "We lose" if L > W else "Draw"

print(battle("Cheeseburger with fries", "Cheeseburger with Fries"))
