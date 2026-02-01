def scale_image(size, scale):
    return "x".join(list(map(lambda x: str(int(int(x) * scale)), size.split("x"))))

print(scale_image("1024x768", 0.5))