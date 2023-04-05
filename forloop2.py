li = ['xyz', 'nitin', 'ray', 'lol', 'trert']
p = []
for i in li:
	if i == i[::-1]:
		p.append(i)
print(p)