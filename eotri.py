for i in range(5):
	for k in range(5-i):
		print(" ",end="")
	for j in range(i):
		if i%2==0:
			print("0",end=" ")
		else:
			print("1",end=" ")
	print()