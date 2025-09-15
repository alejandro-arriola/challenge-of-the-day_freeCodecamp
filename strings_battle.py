** start of main.py **

def battle(my_army, opposing_army):
    def check_unit(unit):
        if '0' <= unit <= '9':
            unit = int(unit)
        elif 'a' <= unit <= 'z':
            unit = ord(unit) - ord('a') + 1
        elif 'A' <= unit <= 'Z':
            unit = ord(unit) - ord('A') + 27
        else:
            unit = 0
        return unit

    if len(my_army) > len(opposing_army):
        return "Opponent retreated"
    elif len(my_army) < len(opposing_army):
        return "We retreated"
    
    my_wins = 0
    ur_wins = 0

    for my_unit, ur_unit in zip(my_army, opposing_army):
        my_unit = check_unit(my_unit)
        ur_unit = check_unit(ur_unit)
        if my_unit > ur_unit:
            my_wins += 1
        elif my_unit < ur_unit:
            ur_wins += 1

    return "We won" if my_wins > ur_wins else ("We lost" if my_wins < ur_wins else "It was a tie")

print(battle("C@T5", "D0G$"))

** end of main.py **

