
def OpenFile(file_name):
	f=open(file_name)
	return f
	
def Daysale(file_pointer):
	file_pointer.seek(0)
	day_sale={}
	
	h=file_pointer.readline()
		
	data=file_pointer.readlines()
	for i in data:
		xx=i.split('\n')[0].split(",")
		sale=xx[14]
		day=xx[11]
		
		if day_sale.get(day)==None:
			day_sale[day]=float(sale)	
		else:
			day_sale[day]+=float(sale)
	day_sale_result={ k:float("{:.2f}".format(v)) for k,v in sorted(day_sale.items(), key=lambda item: item[1],reverse=True)}
	return day_sale_result

def Monthsale(file_pointer):
	file_pointer.seek(0)
	month_sale={}
	
	h=file_pointer.readline()
		
	data=file_pointer.readlines()
	for i in data:
		xx=i.split('\n')[0].split(",")
		sale=xx[14]
		month=xx[9]
		
		if month_sale.get(month)==None:
			month_sale[month]=float(sale)	
		else:
			month_sale[month]+=float(sale)
	month_sale_result={ k:float("{:.2f}".format(v)) for k,v in sorted(month_sale.items(), key=lambda item: item[1],reverse=True)}
	return month_sale_result

def OrderPerMonth(file_pointer):
	file_pointer.seek(0)
	month_sale={}
	
	h=file_pointer.readline()
		
	data=file_pointer.readlines()
	for i in data:
		xx=i.split('\n')[0].split(",")
		
		month=xx[9]
		
		if month_sale.get(month)==None:
			month_sale[month]=1	
		else:
			month_sale[month]+=1
	month_sale_result={ k:int(v) for k,v in sorted(month_sale.items(), key=lambda item: item[1],reverse=True)}
	return month_sale_result
def salePerYear(file_pointer):
	file_pointer.seek(0)
	year_sale={}
	
	h=file_pointer.readline()
		
	data=file_pointer.readlines()
	for i in data:
		xx=i.split('\n')[0].split(",")
		sale=xx[14]
		year=xx[10]
		
		if year_sale.get(year)==None:
			year_sale[year]=float(sale)	
		else:
			year_sale[year]+=float(sale)
	month_sale_result={ k:float("{:.2f}".format(v)) for k,v in sorted(year_sale.items(), key=lambda item: item[1],reverse=True)}
	return month_sale_result
def Totalsale(file_pointer):
	file_pointer.seek(0)
	total_sale={}
	
	h=file_pointer.readline()
		
	data=file_pointer.readlines()
	for i in data:
		xx=i.split('\n')[0].split(",")
		sale=xx[14]
				
		if total_sale.get("Total sale")==None:
			total_sale["Total sale"]=float(sale)	
		else:
			total_sale["Total sale"]+=float(sale)
	month_sale_result={ k:float("{:.2f}".format(v)) for k,v in sorted(total_sale.items(), key=lambda item: item[1],reverse=True)}
	return month_sale_result

def Countrysale(file_pointer):
	file_pointer.seek(0)
	country_sale={}
	
	h=file_pointer.readline()
		
	data=file_pointer.readlines()
	for i in data:
		xx=i.split('\n')[0].split(",")
		sale=xx[14]
		country=xx[8]
		
		if country_sale.get(country)==None:
			country_sale[country]=float(sale)	
		else:
			country_sale[country]+=float(sale)
	day_sale_result={ k:float("{:.2f}".format(v)) for k,v in sorted(country_sale.items(), key=lambda item: item[1],reverse=True)}
	return day_sale_result
def plot(d,hue):
	import seaborn as sns
	import matplotlib.pyplot as plt
	import pandas
	df=pandas.DataFrame(d.items())
	names = list(d.keys())
	values = list(d.values())
	plt.bar(range(len(d)), values, tick_label=names)
	plt.show()
if __name__=='__main__':
	f=OpenFile('G:\\Hopping Minds\\Assignment\\clean_data.csv')
	weekday_sale_result=Daysale(f)
	month_sale_result=Monthsale(f)
	order_per_month_result=OrderPerMonth(f)
	year_sale_result=salePerYear(f)
	total_sale_result=Totalsale(f)
	country_sale_result=Countrysale(f)
	print(weekday_sale_result)
	print(month_sale_result)
	print(order_per_month_result)
	print(year_sale_result)
	print(total_sale_result)
	print(country_sale_result)
	plot(year_sale_result,"Year Wise Sale")
	f.close()
	