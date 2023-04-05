d = {
    'Gfg':{"a":7,"b":9,"c":12},
    'is':{"a":15,"b":19,"c":20},
    'Best':{"a":5,"b":10,"c":2}
    }
#temp = input("Enter key: ")
temp = 'b'
res = []
# output : [9,10,19]
for i,k in d.items():
    for j,v in k.items():
        if j == temp:
            res.append(k[j])
print(sorted(res))            

# or
ans = []
for k,v in d.items():
    if temp in v:
        ans.append(v[temp])     
print(sorted(ans))