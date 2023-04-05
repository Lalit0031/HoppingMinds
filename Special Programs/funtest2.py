import time
def wish(name):
	h=time.localtime().tm_hour
	m=time.localtime().tm_min
	tt=float(str(h)+'.'+str(m))
	if tt>=12:
		print(f"Hello {name}, Good Afternoon!!!")
	else:
		print(f"Hello {name}, Good Morning!!!")
		
u=input("Enter your username...")
wish(u)
	
