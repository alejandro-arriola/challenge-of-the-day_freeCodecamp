from datetime import datetime

def odd_or_even_day(timestamp):
    date = datetime.fromtimestamp(timestamp/100)

    return "even" if date.day % 2 == 0 else "odd" 

print(odd_or_even_day(1769472000000))