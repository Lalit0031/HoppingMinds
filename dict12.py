data = {101:['xyz_8','pp_3','cc_6'],
        102:['xyz_5','pp_1','cc_2'],
        103:['xyz_3','pp_4','cc_9'],
        104:['xyz_6','pp_2','cc_3'],
        }
print("before : ",data)
d = {}
for k,v in data.items():
        l = []
        for i in v:
                x = i.split("_")
                l = l+[(i,x[1])]
        d[k] = l                    
        
res = {k: sorted(v,key = lambda x:int(x[1])) for k,v in d.items()}


dd  = {}

for k,v in res.items():
        pp = []
        for d in v:
                pp+=[d[0]]
        dd[k] = pp
        
print("After : ",dd)