f = open("test_file.txt",'a')
f.write("Alphabet pattern\n")
y=65
for i in range(1,5):
	for k in range(5-i):
		f.write(" ")
	for j in range(i):
		f.write(chr(y))
		y=y+1
	f.write("\n")