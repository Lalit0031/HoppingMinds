import os

f = open("Code_runner.txt", 'r')
x = f.readlines()
for i in x:
    z = i.split('\n')[0]
    a = open(z,'r')
    xx = a.read()
    rr  = open('New_file.txt','a')
    rr.write(f"------{z}------\n")
    rr.write(xx)
    rr.write("\n")
    rr.write("------output------\n")
    os.system("py "+z)
    rr.write("**********************************************************\n")
    