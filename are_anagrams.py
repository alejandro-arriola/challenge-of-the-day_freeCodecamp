def are_anagrams(str1, str2):
    return "".join(sorted(str1.lower())) == "".join(sorted(str2.lower()))

print(are_anagrams("School master", "The classroom"))