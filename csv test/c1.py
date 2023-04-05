import csv
file = "G:\\Hopping Minds\\csv test\\c1.csv"
# writing
"""with open(file, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Id', 'Name', 'Dept', 'Address'])
    n = int(input("Enter no. of item : "))
    
    for i in range(n):
        id = input("Enter Id : ")
        name = input("Enter Name : ")
        dept = input("Enter Department : ")
        add = input("Enter Address : ")
        w.writerow([id,name,dept,add])
"""

# reading
"""res = open(file,'r')
print(res.readline())
print(res.read())"""


res = open(file,'r')
print(list(csv.reader(res)))

