s = "leet"
d = {}

for i in s:
    if d.get(i) == None:
        d[i] = 1
    else:
        d[i]+=1

for k,v in d.items():        
    if v == 1:
        print(k,"is the 1st non repeating character")
        break