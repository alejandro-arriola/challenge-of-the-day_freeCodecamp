def factorial(n):
    if n > 1:
        f = 1
        for i in range(2, n + 1):
            f *= i
        return f

    return 1

print(factorial(0))