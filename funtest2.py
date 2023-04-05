import time
def wish(name):
	h=time.localtime().tm_hour
	m=time.localtime().tm_min
	tt=float(str(h)+'.'+str(m))
	if tt>=12:
		print(f"Hello {name}, Good Afternoon!!!")
	else:
		print(f"Hello {name}, Good Morning!!!")
		
def bill(name,**p):
	wish(name)
	sum = 0.0
	print("\nProduct Name\t\t\tPrice")
	for k,v in p.items():
		print(f"{k}\t\t\t\t{v}")
		sum =sum + v
	print(f"Total\t\t\t\t{sum}")
	print()
	print("****Thanks for shopping with us****")

bill("lalit",phone=1000,ball=133,pen=10000)

