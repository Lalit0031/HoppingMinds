# input  : n = 3
# string : paradox
# we mirror chr from position 3 to end
# output : paizwlc
 
# input  : n = 6 
# string : pneumonia
# we mirror chr from position 6 to end
# output : pneumlmrz

data = {'a': 'z', 'b': 'y', 'c': 'x', 
        'd': 'w', 'e': 'v', 'f': 'u', 
        'g': 't', 'h': 's', 'i': 'r', 
        'j': 'q', 'k': 'p', 'l': 'o', 
        'm': 'n', 'n': 'm', 'o': 'l', 
        'p': 'k', 'q': 'j', 'r': 'i', 
        's': 'h', 't': 'g', 'u': 'f', 
        'v': 'e', 'w': 'd', 'x': 'c', 
        'y': 'b', 'z': 'a'
        }
#n = 3
#s = 'paradox'

n = 6
s = 'pneumonia'
x = s[:n-1]
y = s[n-1:]
z = ''
d = {}

for i in y:
    z = z + data[i]
    
print(x+z)
    
