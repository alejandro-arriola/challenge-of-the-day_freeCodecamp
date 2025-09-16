def too_much_screen_time(hours):
    if sum(hours) / len(hours) >= 6:
        return True

    for day in range(len(hours)):
        if hours[day] >= 10:
            return True
        
        if day + 2 < 7 and (hours[day] + hours[day+1] + hours[day+2])/3 >= 8:
            return True

    return False

print(too_much_screen_time([1, 2, 3, 10, 2, 1, 0]))