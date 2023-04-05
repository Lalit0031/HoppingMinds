a = "abcdefghijklmnopqrstuvwxyz"
b = "zyxwvutsrqponmlkjihgfedcba"

data = {}
# size should be same while using zip function.
y = dict(zip(a,b))
print(y)

for x in range(len(a)):
    data[a[x]] = b[x]
    
print(data)