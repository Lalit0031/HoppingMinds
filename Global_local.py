x = 10 # global

def add(a,b):
    x = 15 # local
    # preference is given to local variable
    print(a+b)
    print(x)

def fun1():
    global x # this will update the value of global variable
    x = 55
    print(x)

def fun2():
    print(x)

fun2()
fun1()
