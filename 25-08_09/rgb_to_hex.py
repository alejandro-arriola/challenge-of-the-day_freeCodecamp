def rgb_to_hex(rgb):
    rgb = rgb.split(", ")
    rgb = [int(rgb[0][4:7]), int(rgb[1]), int(rgb[2][:-1])]

    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

print(rgb_to_hex("rgb(173, 216, 230)"))