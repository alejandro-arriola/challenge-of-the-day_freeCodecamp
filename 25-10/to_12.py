def to_12(time):
    hour = int(time[:2])
    posfix = ""

    if hour < 12:
        posfix = " AM"
        hour = 12 if hour == 0 else hour
    else:
        posfix = " PM"
        hour -= 12

    return str(hour) + ":" + time[2:] + posfix 

print(to_12("0030"))