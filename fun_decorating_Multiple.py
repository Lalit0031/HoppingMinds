def upper_decore(function):
    def wrapper():
        func= function()
        make_upper = func.upper()
        return make_upper
    return wrapper

def split(function):
    def wrapper():
        func = function()
        split = func.split()
        return split
    return wrapper

@split
@upper_decore
def say_hi():
    return "hello all"


print(say_hi())
    