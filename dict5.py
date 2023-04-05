x = "A man,a plan, a canal:panama"
y = x.lower()

new = ""
for i in y:
    if i.isalnum():
        new = new + i

if new == new[::-1] :
    print("it's a Palindrome")
else:
    print("it's not Palindrome")