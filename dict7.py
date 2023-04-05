d = {"Gfg":[5,7,5,4,5],"is":[6,7,4,3,3],"Best":[9,9,6,5,5]}

# find key with max unique values :=> is

temp = 0
flag = 0
res = ""
for i,v in d.items():
    count = 0
    x = {}
    for j in v:
        if x.get(j) == None:
            x[j] = 1
        else:
            x[j]+=1
    
    for k in x.keys():
        if x[k] == 1:
            count = count + 1
    if temp < count:
             temp = count 
    #temp = max(temp,count)
    if temp == count:
        flag = 1
        res = i
    else:
        flag = 0
    
print(res, temp)

            