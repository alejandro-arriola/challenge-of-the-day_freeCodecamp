def tire_status(pressures_psi, range_bar):
    range_bar = list(map(lambda v: v * 14.5038, range_bar))
    response = []

    for t in pressures_psi:
        if t < range_bar[0]:
            response.append("Low")
        elif t <= range_bar[1]:
            response.append("Good")
        else:
            response.append("High")
        
    return response

print(tire_status([32, 28, 35, 29], [2, 3]))