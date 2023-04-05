f = open("test_file.txt",'a')
f.write("Star pattern\n")
for i in range(5,0,-1):
    for j in range(i):
        f.write("* ")
    f.write("\n")
f.close()