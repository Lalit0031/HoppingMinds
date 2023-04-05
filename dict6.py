f = "baloon"
g = "nlaebolko"
d = {}
for i in g:
    if d.get(i) == None:
        d[i] = 1
    else:
        d[i] = d[i] + 1
        
print(d)

b = {}
for i in f:
    if b.get(i) == None:
        b[i] = 1
    else:
        b[i] = b[i] + 1

print(b)

