import random

randomlist = random.sample(range(1, 10), 5)
print(randomlist)
x = 3
i = 0
result = False

for value in randomlist:
    if value == x:
        print("Значение есть в списке", i)
        result = True
    i = i + 1

if result == False:
    print("Значения нет в списке")