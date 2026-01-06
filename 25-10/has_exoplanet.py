def has_exoplanet(readings):
    readings = [ord(value) - ord('A') + 10 if value.isalpha() else int(value) for value in list(readings)]
    threshold = (sum(readings) / len(readings)) * 0.8
    
    return any(value <= threshold for value in readings)

print(has_exoplanet("665544554"))