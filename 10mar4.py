a = [1,2,3,4,5,0]
b = [5,6,7,8,9,11]

for i in a:
    if i in b:
        print(f"{i} is common in both the lists.")
        
        
# alternative way
    
a1 = set(a)
b1 = set(b)

x = a1.intersection(b1)
for i in x:
    print(f"{i} is common in both the lists.")