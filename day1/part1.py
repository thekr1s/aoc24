import os
BLUE = '\033[94m'
CYAN = '\033[96m'
GREEN = '\033[92m'
ORANGE = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def string_to_ints(str, separator):
    s = str.strip().split(separator)
    a = []
    for n in s:
        a.append(int(n.strip()))
    return a

dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")
lines = []
a1=[]
a2=[]
for l in f.readlines():
    l = l.replace("   ", " ");
    lines.append(l.strip())
    s = l.strip().split(" ")
    a1.append(s[0])
    a2.append(s[1])
        
a1.sort()
a2.sort()
sum = 0
for i, a in enumerate(a1):
    sum += abs(int(a2[i]) - int(a))
    pass
print(sum)
    
    
    