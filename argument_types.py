# Positional Argument
def sum(a,b,c,d):
	print(a+b+c+d)
#sum(1,2,3,4)


# Keyword Argument
def sum(a,b,c,d):
	print(a+b+c+d)
#sum(a=1,b=2,c=3,d=4)


# default argument
def sum(a,b,c=10,d=1):
	print(a+b+c+d)
#sum(1,1)
#sum(2,3,3,4)
#sum(2,2,3)


# variable length argument
def sum(*n):
	print(n)
	s = 0
	for i in n:
		s=s+i
	print("sum : ",s)

#sum(10)
#sum(1,2,3,4)
#sum(22,33,44,55,66,88)

# variable length keyword argument

def bill(**p):
	print(p)

#bill(phone=122222,pen=1133,gun=11222,van=123)