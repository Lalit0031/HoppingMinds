f = open("Emp_data.txt",'a')

name = input("Enter name : ")
age = int(input("Enter age : "))
sal = float(input("Enter salary : "))
ms = bool(int(input("Enter Marital status (1 => marrid , 0=> Unmarrid) : ")))

f.write("**************** New User ***********************\n")
f.write(f'''Hello {name}! 
Your age is {age} and your salary is {sal}.
your marital status is {ms}.\n''')
f.close()



