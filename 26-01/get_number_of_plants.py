import math

def get_number_of_plants(field_size, unit, crop):
    crop_table = {
        "corn" : 1,
        "wheat" : 0.1,
        "soybeans" : 0.5,
        "tomatoes" : 0.25,
        "lettuce" : 0.2, 
    }

    unit_table = {
        "acres" : 4046.86,
        "hectares" : 10000,
    }

    return math.floor(field_size * unit_table[unit] / crop_table[crop])

print(get_number_of_plants(1, "acres", "corn"))