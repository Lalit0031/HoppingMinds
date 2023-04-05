def decor_wish(func):
    def inner(name):
        if name.lower() == 'rajat':
            print(f"Hello {name} going home.")
        else:
            func(name)
    return inner


@decor_wish
def wish(name):
    print(f"Hello {name} going to part.")
    
wish("lalit")
wish("Rajat")
wish("ram")