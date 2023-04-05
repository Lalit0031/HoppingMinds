name = input("enter your name :")
a = int(input("Enter Subject marks 1 : "))
b = int(input("Enter Subject marks 2 : "))
c = int(input("Enter Subject marks 3 : "))
avg = float((a+b+c)/3)
g = ""
if avg > 90 :
	g="A"
elif avg > 80 and avg<=90: 
	g="B"
elif avg > 70 and avg<=80:
	g="C"
elif avg > 60 and avg<=70:
	g="D"
else:
	g="E"
print(f"\nHello {name} !! \nAccording to your percentage ,i.e, {avg} , your Grade is {g}  ")
