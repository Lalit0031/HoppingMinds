import time
from datetime import datetime as dt
path="C:\\Windows\\System32\\drivers\\etc\\hosts"
redirect="\n127.0.0.1"
website_list=["www.facebook.com","https://www.facebook.com/"]
while True:
	if dt(dt.now().year,dt.now().month,dt.now().day,12,10)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,12,43):
		with open(path,'r+') as f:
			content=f.read()
			for website in website_list:
				if website in content:
					pass
				else:
					f.write(redirect+" "+website)
						
		print("Working Hours.....")
		time.sleep(1)
	else:
		with open(path,'r+') as f:
			content=f.readlines()
			f.seek(0)
			for line in content:
				
				if not any(website in line for website in website_list):
					f.write(line)
			f.truncate()
			
		print("Fun  Hours....")
		time.sleep(1)
	