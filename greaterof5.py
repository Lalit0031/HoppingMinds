a = int(input("Enter a : "))
b = int(input("Enter b: "))
c = int(input("Enter c : "))
d = int(input("Enter d : "))
e = int(input("Enter e : "))
if a>b and a>c and a>d and a>e:
	print("a is greater ")
elif  b>c and b>d and b>e:
	print("b is greater")
elif c>d and c>e:
	print("c is greater ")
elif d>e:
	print("d is greater")
else:
	print("e is greater")
