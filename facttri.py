from math import factorial as fact
n =5
for i in range(n):
	for k in range(n-i+1):
		print(" ",end="")
	for j in range(i+1):
		v = fact(i)//(fact(j)*fact(i-j))
		print(int(v),end=" ")
	print()