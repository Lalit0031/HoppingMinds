import os

f = open("Code_runner.txt", 'r')
x = f.readlines()
for i in x:
    print(i)
    os.system(i)
f.close()