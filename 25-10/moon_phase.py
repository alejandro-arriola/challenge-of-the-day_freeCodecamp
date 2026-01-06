from datetime import date
import math

def moon_phase(date_string):
    base_date = date(2000, 1, 6)
    given_date = date.fromisoformat(date_string)
    delta = math.floor((given_date - base_date).days / 7) % 4
    return ["New", "Waxing", "Full", "Waning"][delta]

print(moon_phase("2000-01-13"))