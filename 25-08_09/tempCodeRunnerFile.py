def are_anagrams(str1, str2):
    return "".join(sorted(str1)) == "".join(sorted(str2))

print(are_anagrams("School master", "The classroom"))