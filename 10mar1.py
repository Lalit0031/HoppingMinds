arr = [1,2,3,4,1,2,3,4,1,5,4,3,2]

new = []
for i in arr:
    if i not in new:
        new.append(i)

print(new)