def fun1():
    print("I am outer function.")
    
    def fun2():
        print("I am innner function.")
        
    print("outer calling inner.")
    return fun2()

# function aliasing
f = fun1
f()