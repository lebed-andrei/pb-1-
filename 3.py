x = [1, 'z']
y = 0
z = []
z.append(x[len(x) - 1])
while y < len(x) - 1:
    y += 1
    z.append(x[len(x) - 1 - y])
print (z)