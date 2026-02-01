#I first took a recursive approach, but the test took a long time to complete and after completion it 'failed' despite the output being correct
def nth_fibonacci(n):
    a, b = 0, 1

    for _ in range(3, n + 1):
        a, b = b, a + b

    return b 

print(nth_fibonacci(40))