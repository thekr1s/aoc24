#!/bin/python
from dataclasses import dataclass
import os
dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")
lines = []
for l in f.readlines():
    lines.append(l.strip())
    
    
sum = 0
ru = []
for l in lines:
    if "|" in l:
        ru.append(l.split("|"))
    else:
        for r in ru: 
            a = l.find(r[0])
            b = l.find(r[1])
            if a != -1 and b != -1:
                if a > b:
                    break
        else:
            if l != "":
                s = l.split(",")
                m = (len(s)-1)/2
                sum += int(s[int(m)])


    pass
print(sum)
    
    
    