def goldilocks_zone(mass):
    luminosity_squared = (mass ** 3.5) ** 0.5

    return [ round(luminosity_squared * 0.95, 2), round(luminosity_squared * 1.37, 2) ]

print(goldilocks_zone(0.5))