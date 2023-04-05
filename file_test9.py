# get username and password from a user and check if it's in thefile
import time
f = open('user_data.txt', 'r')
data = f.readlines()
print(data)

get_user = input("Enter Username : ")

for i in data:
    a = i.split("\n")[0].split(',')
    username = a[0]
    password = a[1]
    
    if get_user == username:
        get_pass = input("Enter Password : ")
        while get_pass != password:
            get_pass = input("Re-enter Password : ")
            time.sleep(1)
        else:
            print("Welcome!! to the system.")
            break
else:
    print("Wrong Username")
            
    
    