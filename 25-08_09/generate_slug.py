def generate_slug(str):
    str = str.strip().lower()
    str = "".join([char for char in str if char.isalpha() or char.isdigit() or char == " "])
    str = " ".join(str.split())
    str = str.replace(" ", "%20")

    return str

print(generate_slug("  ?H^3-1*1]0! W[0%R#1]D  "))