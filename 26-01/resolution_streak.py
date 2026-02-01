def resolution_streak(days):
    count = 0

    for day in days:
        count += 1

        if day[0] >= 10000 and day[1] <= 120 and day[2] >= 5:
            continue
        else:
            return f"Resolution failed on day {count}: {count - 1} day streak." 

    return f"Resolution on track: {count} day streak."

print(resolution_streak([[15000, 110, 8], [12300, 60, 13], [10100, 120, 4], [9000, 125, 4]]))