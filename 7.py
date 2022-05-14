d = "строка подстрока"
dict = {}
for c in d:
    if c in dict:
        dict[c] += 1
    else:
        dict[c] = 1

print(dict)