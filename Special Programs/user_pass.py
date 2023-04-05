import sys
import time
import os

user = 'root'
Password = '1234'

u = input("Enter Username : ")
if u == user:
    p = input("Enter Password : ")
    while p != Password:
        p = input("Re-enter Password : ")
        time.sleep(1)
    else:
        print("Welcome!! to the system.")
else:
    print("Wrong Username")
        