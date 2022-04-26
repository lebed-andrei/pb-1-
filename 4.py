x=[-9,2,9,100,5]
N = len(x)      

for i in range(0, N-1):   
    for j in range(0, N-1-i):  
        if x[j] > x[j+1]:
            x[j], x[j+1] = x[j+1], x[j]

print(x)

