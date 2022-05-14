mm = [33, -59, 724, 513, 0], [-4325, 5543, 532, 49029, "k"]
trans_mm = [[0 for j in range(len(mm))] for i in range(len(mm[0]))]
for i in range(len(mm)):
    for j in range(len(mm[0])):
        trans_mm[j][i] = mm[i][j]
print(trans_mm)