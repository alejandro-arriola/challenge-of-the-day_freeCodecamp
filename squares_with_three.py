** start of main.py **

def squares_with_three(n):
    counter = 0

    for i in range(1, n):
        if '3' in str(i * i):
            counter += 1

    return counter

print(squares_with_three(1000))

** end of main.py **

