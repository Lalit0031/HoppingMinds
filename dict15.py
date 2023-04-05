a = "abcdefghijklmnopqrstuvwxyz"
b = "zyxwvutsrqponmlkjihgfedcba"
y = dict(zip(a,b))

c = a.upper()
d = b.upper()
x = dict(zip(c,d))

y.update(x)
print(y)