from copy import deepcopy
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
for l in f.readlines():
    lines.append(l.strip())
    
    
sum = 0
def is_safe( s):
    for i, v in enumerate(s[1:]):
        i+=1
        d = v-s[i-1]
        inc = False
        if d > 0:
            inc = True 
        if i == 1:
            p = inc
        d = abs(d)
        if (d == 0 or d > 3) or  p != inc:
            break
        p = inc
    else:
        return True
    return False

for l in lines:
    s = string_to_ints(l, " ")
    for i,_ in enumerate(s):
        s1=deepcopy(s)
        del s1[i]
        if is_safe(s1):
            sum += 1
            break

print(sum)
    
    
    