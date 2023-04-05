f = open("test_file.txt", 'a')
f.write("Star pattern\n")
for i in range(10):
    for k in range(10-i):
        f.write(" ")
    for j in range(5):
        f.write("*")
    for k in range(10-i):
        f.write("*")
    for j in range(5):
        f.write("*")
    for k in range(10-i):
        f.write("*")
    for j in range(5):
        f.write("*")
    for k in range(10-i):
        f.write(" ")
    for j in range(5):
        f.write("*")
    f.write("\n")
 
for i in range(3):
	for j in range(30):
		f.write("*")
	f.write("\n")
for i in range(10,0,-1):
	for k in range(10-i):
		f.write(" ")
	for j in range(5):
		f.write("*")
	for k in range(10-i):
		f.write("*")
	for j in range(5):
		f.write("*")
	for k in range(10-i):
		f.write(" ")
	for j in range(5):
		f.write("*")
	for k in range(10-i):
		f.write(" ")
	for j in range(5):
		f.write("*")
	f.write("\n")
f.close()