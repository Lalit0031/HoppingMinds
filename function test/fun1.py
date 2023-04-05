def palindrom(a):
    y = a.lower()
    new = ""
    for i in y:
        if i.isalnum():
            new = new + i
    if new == new[::-1]:
        print("It's Palindrom.")
    else:
        print("Not palindrom.")
        
  
  
    
x = "A man,a plan, a canal:panama"
palindrom(x)