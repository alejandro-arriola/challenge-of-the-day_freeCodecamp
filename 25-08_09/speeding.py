from functools import reduce

def speeding(speeds, limit):
    n_vehicles = reduce(lambda acc, speed: acc + 1 if speed > limit else acc, speeds, 0)

    if n_vehicles == 0:
        return [ 0, 0 ]

    avg_speeding = int(
        reduce(lambda acc, speed: acc + speed, 
            map(lambda speed: speed - limit, 
                filter(lambda speed: speed > limit, speeds)))
    ) / n_vehicles

    return [ n_vehicles, avg_speeding ]

print(speeding([61, 81, 74, 88, 65, 71, 68], 70))