f = open("test_file.txt",'w')
f.write("Star pattern\n")
for i in range(1,6):
    for j in range(i):
        f.write("*")
    
    f.write("\n")

f.close()