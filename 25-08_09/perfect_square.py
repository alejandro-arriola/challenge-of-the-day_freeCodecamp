def is_perfect_square(n):
    if n < 0:
      return False
    square = n ** 0.5
    return square == int(square)



