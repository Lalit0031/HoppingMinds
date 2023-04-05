f = open("test_file1.txt",'w')
l = ['abs\n','pqr\n','xyz\n']
f.writelines(l)
f.close()