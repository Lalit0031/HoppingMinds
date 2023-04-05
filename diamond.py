import sys
sys.stdout = open('New_file.txt','a')
for i in range(5):
	for k in range(5-i):
		print(" ",end="")
	for j in range(i):
		print("*",end=" ")
	print()
for i in range(5,0,-1):
	for k in range(5-i):
		print(" ",end="")
	for j in range(i):
		print("*",end=" ")
	print()