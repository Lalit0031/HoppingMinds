l = [4,6,6,4,2,2,4,8,5,8]

# output: {4:[4,4,4],6:[6,6],2:[2,2],8:[8,8],5:[5]}
 
d = {}
for j in l:
    if d.get(j) == None:
        d[j] = [j]
    else:
        d[j].append(j)
print(d)

# optimized 

b = {}
for i in set(l):
    b[i] = [i]*l.count(i)
print(b)