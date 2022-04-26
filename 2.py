from numpy import random
x=random.randint(100, size=(30))

for i in x:
    if int(i) % 2 == 0:
        print(i)
