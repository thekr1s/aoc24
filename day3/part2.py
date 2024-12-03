#!/bin/python
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

def is_anabled(s, curr):
    e = s.rfind("do()")
    d=s.rfind("don't()")
    if e == -1 and  d == -1:
        return curr
    elif e == -1:
        return False
    elif d == -1:
        return True
    else:
        return d < e 
    
dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")
lines = []
for l in f.readlines():
    lines.append(l.strip())
    
st="mul(*,*)"
sum = 0
enable=True
for l in lines:
    pos = 0
    i=0
    a = ''
    b = ''
    do = l.find("do()")
    dn = l.find("don't()")
    for c in l:
        if i == 4 and c.isdigit(): 
            a+=c
        elif i == 4 and c == ',':
            i+=1
        elif i == 5 and c.isdigit(): 
            b+=c
        elif i == 5 and c == ')':
            enable = is_anabled(l[0:pos], enable)
            if enable:
                sum += int(a)*int(b)
                print(GREEN, end="")
            else:
                print(RED, end="")

            print(f"mul({a},{b})")
            a=''
            b=''
            i=0
        elif st[i]==c:
            i+=1
        elif c == st[0]:
            a=''
            b=''
            i=1
        else:
            a=''
            b=''
            i=0
        pos+=1
print(sum)
    
    
    