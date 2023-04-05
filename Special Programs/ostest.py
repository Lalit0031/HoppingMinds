import os 
import time
fname=input("Enter File name which you want to open")
if os.path.exists(fname):
	print(os.listdir("."))
	print("I am opening file....")
	time.sleep(1)
	f=open(fname)
	print(f.read())
else:
	print("Please check name file is not there....")