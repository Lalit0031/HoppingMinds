import os
def checkfile(filename):
	r=os.path.isfile(filename)
	return r
def readfile(fname):
	f=open(fname)
	return f.read()
def palin(text):
	if text==text[::-1]:
		return True
	else:
		return False
	
fname=input("Enter File name to check..")
rr=checkfile(fname)
if rr==True:
	data=readfile(fname)
	result=palin(data)
	print(result)
else:
	print("File not there please check file anme you enterd.....")
	
	
	