def anagram(a,b):
    x = {}
    y = {}
    if len(a) == len(b):
        for i in a:
            if x.get(i) == None:
                x[i] = 1
            else:
                x[i] = x[i] + 1
        

        for i in b:
            if y.get(i) == None:
                y[i] = 1
            else:
                y[i] = y[i] + 1
       

        if x == y:
            print("It's Anagram")
        else:
            print("Not Anagram") 
         
    else:
        print("Not Anagram")

x = input("Enter 1st value : ")
y = input("Enter 2nd value : ")
anagram(x,y)

