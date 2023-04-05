x = "ababcbabcabcacbbadbcdcbcdbdabbadcdcabcadbc"
d = {}
for i in x:
    if d.get(i) == None:
        d[i] = 1
    else:
        d[i] = d[i] + 1   
        
print(d)
        