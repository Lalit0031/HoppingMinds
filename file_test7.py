
# tell() will tell location of the curser in a file.
# seek() will shift location of the curser 

f = open('Emp_data.txt','r')
y = f.seek(14)
print(y)
z = f.tell()
print(z)
