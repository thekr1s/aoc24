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
    
    
sum = 0
for l in lines:
    pass
print(sum)
    
    
    