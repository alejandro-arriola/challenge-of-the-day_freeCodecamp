def get_bingo_letter(n):
    dic = { 
        n >= 1 : "B",
        n >= 16 : "I",
        n >= 31 : "N",
        n >= 46 : "G",
        n >= 61 : "O",
    }

    return dic[True]

print(get_bingo_letter(75))