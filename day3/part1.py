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

dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")
lines = []
for l in f.readlines():
    lines.append(l.strip())
    
st="mul(*,*)"
sum = 0
for l in lines:
    i=0
    a = ''
    b = ''
    for c in l:
        if i == 4 and c.isdigit(): 
            a+=c
        elif i == 4 and c == ',':
            i+=1
        elif i == 5 and c.isdigit(): 
            b+=c
        elif i == 5 and c == ')':
            sum += int(a)*int(b)
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

print(sum)
    
    
    