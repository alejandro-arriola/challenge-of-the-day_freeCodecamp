def get_headings(csv):
    return list(map(str.strip, csv.split(",")))

print(get_headings("username , email , signup date "))