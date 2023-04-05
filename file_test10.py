# Q1: total salary based on dept
# Q2: total salary based on gender
# Q3: total salary based on gender in a particular dept
# DATA SAMPLE : eno,name,dept,gender,sal

f = open('Emp_data1.txt', 'r')
h = f.readline()
data = f.readlines()

q1 = {}
q2 = {}
q3 = {}
ts = 0
for i in data:
    a = i.split("\n")[0]
    b = i.split(",")
    dept = b[2]
    g = b[3].lower()
    sal = b[4]
    ts = ts+float(sal)
    key = dept+"_"+g
    if q1.get(g) == None:
        q1[g] = float(sal)
    else:
        q1[g] += float(sal)
    if q2.get(dept) == None:
        q2[dept] = float(sal)
    else:
        q2[dept] += float(sal)
    if q3.get(key) == None:
        q3[key] = float(sal)
    else:
        q3[key] += float(sal)
        
print("Total budget : ",ts)
print("Total budget based on gender : ",q1)
print("Total budget based on deptartment : ",q2)
print("Total budget based on gender as per department :",q3)
   
   
import matplotlib.pyplot as plt
import seaborn as sns 

p = [float(i) for i in q1.values()]
sns.barplot(x=list(q1.keys()),y = p)
plt.title("Budget based on Gender")
plt.show()

p = [float(i) for i in q2.values()]
sns.barplot(x=list(q2.keys()),y = p)
plt.title("Budget based on Department")
plt.show()

p = [float(i) for i in q3.values()]
sns.barplot(x=list(q3.keys()),y = p)
plt.title("Budget based on Gender as per Department")
plt.show()