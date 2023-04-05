x = input("Enter somthing : ")
a = "0123456789"
for i in range(len(x)):
	if x[i] in a:
		print(x[i],end="")

