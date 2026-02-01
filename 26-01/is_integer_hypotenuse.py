def is_integer_hypotenuse(a, b):
    h = (a * 2 + b * 2) ** 0.5
    return h == int(h)