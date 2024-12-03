#!/bin/python
import re
import os
dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")
lines = []
for l in f.readlines():
    lines.append(l.strip())
    
st="mul(*,*)"
sum = 0
enable=True
for l in lines:
    for r in re.finditer("mul\((\d*)\,(\d*)\)|do\(\)|don\'t\(\)",l,flags=0):
        s = l[r.regs[0][0]: r.regs[0][1]]
        if s.startswith("mul"):
            if enable:
                a = l[r.regs[1][0]: r.regs[1][1]]
                b = l[r.regs[2][0]: r.regs[2][1]]
                sum += int(a)*int(b)
        elif s.startswith("don"):
            enable = False
        elif s.startswith("do("):
            enable = True
        print(l[r.regs[0][0]: r.regs[0][1]])

print(sum)
    
    
    