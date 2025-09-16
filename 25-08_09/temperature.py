def adjust_thermostat(temp, target):
    return "cool" if temp > target else ("heat" if temp < target else "hold")

print(adjust_thermostat(68, 72))

