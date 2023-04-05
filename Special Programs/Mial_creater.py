from datetime import date

f = open('stu.txt','r')
data = f.readlines()
today = date.today().strftime('%Y-%M-%D')
d = open("mail.txt").read()
for i in data:
    a = i.split('\n')[0].split(',')
    name = a[0]
    rol = a[1]
    att = a[2]
    mail = d.format(date.today(),name,rol,att)
    m = open(f"G:\\Hopping Minds\\mail\\{name}.txt",'w')
    m.write(mail)
    
