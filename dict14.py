# multiple times entries and we have to find the index of every items.
a = "abcbabdadbacc"
d = {}

for i in range(len(a)):
    if d.get(a[i]) == None:
        d[a[i]] = [i]
    else:
        d[a[i]].append(i)
print(d)