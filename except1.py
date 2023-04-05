import traceback
d = {1:12,2:13}
try:
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    print(a//b)
    print(d[10])
except Exception as msg:
    print("Check code .....",msg)
    traceback.print_exc()
else:
    print("Try block executed successfully....")
finally:
    print("I'm immortal......")
    
print("application executed successfully...")