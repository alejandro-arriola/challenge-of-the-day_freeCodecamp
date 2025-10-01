def format_number(number):
    return f"+{number[0]} ({number[1:4]}) {number[4:7]}-{number[7:11]}"

print(format_number("05552340182"))