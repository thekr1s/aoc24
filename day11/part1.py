#!/bin/python
from copy import deepcopy
from dataclasses import dataclass
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

end_stones=[]
def blink(val:int, count:int):
    sval = str(val)    
    l = len(sval)
    if count == 0:
        end_stones.append(val)
    else:
        count -= 1
        if val == 0:
            blink(1, count)
        elif l % 2 == 0:
            blink(int(sval[:int(l/2)]),count)
            blink(int(sval[int(l/2):]),count)
        else:
            blink(val*2024,count)

dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")
lines = []
for l in f.readlines():
    lines.append(l.strip())
    
    
sum = 0
s = string_to_ints(lines[0]," ")
for v in s:
    print("=========================")
    blink(v, 25)    
print(end_stones)
print(len(end_stones))
    
