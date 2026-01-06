def launch_fuel(payload):
    fuel = 0

    while(payload >= 1):
        payload = payload / 5
        fuel = fuel + payload

    return round(fuel, 1) 

print(launch_fuel(243))