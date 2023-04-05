import json as j
def fun(path):
    f = open(path, 'r')
    x = f.readlines()
    d = {}
    for i in x:
        z = i.split('\n')[0].split(',')
        if d.get(z[0]) == None:
            d[z[0]] = z[1]
    return d
path = "G:\\Hopping Minds\\function test\\fun4.txt"
r = fun(path)
res = j.dumps(r,indent=2,separators=(",",":"))
print(res)

            
        
    