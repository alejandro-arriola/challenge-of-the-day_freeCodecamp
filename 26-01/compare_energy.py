def compare_energy(calories_burned, watt_hours_used):
    c = calories_burned * 4184
    w = watt_hours_used * 3600
    return "Workout" if c > w else "Devices" if c < w else "Equal"