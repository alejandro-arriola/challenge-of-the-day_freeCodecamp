def all_unique(s):
    return sorted(list(s)) == sorted(list(set(s)))

print(all_unique("aA"))