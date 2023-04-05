arr = [1,2,5,4,6,7,8,4,2,3,8,9,0]
#new = list(set(sorted(arr)))
new = []
for i in arr:
    if i not in new:
        new.append(i)
        
x = sorted(new)
print(x)

s = x[0]
l = x[len(x)-1]

print("Smallest number : ",s)
print("Largest number : ",l)