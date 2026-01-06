def adjust_thermostat(current_f, target_c):
    target_c = (target_c * 1.8) + 32
    diff = abs(current_f - target_c)

    if(current_f < target_c):
        return f"Heat: {diff:.1f} degrees Fahrenheit"
    
    if(current_f > target_c):
        return f"Cool: {diff:.1f} degrees Fahrenheit"

    return "Hold" #if equal

print(adjust_thermostat(72, 18))