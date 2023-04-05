x = "finding"
y = {}
for i in x:
    if y.get(i) == None:
        y[i] = 1
    else:
        y[i] = y[i] + 1

for i,j in y.items():
    if j != 1:
        print(i,"comes",j,"times")
    
