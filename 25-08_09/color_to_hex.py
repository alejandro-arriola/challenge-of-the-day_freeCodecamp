import random

def generate_hex(color):
    hex_color:str 
    rand = [random.randint(0, 15) for v in range(4)]
    rand = [str(n) if n < 10 else chr(n - 10 + ord('A')) for n in rand]
    rand = "".join(rand)
    
    match color:
        case "red":
            hex_color = "FF" + rand
        case "green":
            hex_color = rand[:2] + "FF" + rand[2:]
        case "blue":
            hex_color = rand + "FF"
        case _:
            hex_color = "Invalid color"

    return hex_color

print(generate_hex("green"))
print(generate_hex("green"))
