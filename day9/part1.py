#!/bin/python
from dataclasses import dataclass
import os

def string_to_ints(str, separator):
    s = str.strip().split(separator)
    a = []
    for n in s:
        a.append(int(n.strip()))
    return a

dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")
lines = []
disk=[]
for l in f.readlines():
    l=l.strip()
    lines.append(l)
    file=True
    id = 0
    for c in l:
        if file:
            disk+=[id]*int(c)
            id+=1
        else:
            disk+=['.']*int(c)
        file=not file


for e in disk:
    print(end=str(e))

n = 0
done=False
for d in reversed(disk):
    n+=1
    print(len(disk)-n)
    if d == '.':
        continue
    for i,e in enumerate(disk):
        e=disk[i]
        if i > len(disk)-n:
            done=True
            break
        if disk[i] == '.':
            disk[i]=d
            disk[len(disk)-n] = '.'
            break
    if done:
        break

sum = 0
for i, e in enumerate(disk):
    print(end=str(e))
    if e != '.':
        sum += e*i



print()
for l in lines:
    pass
print(sum)
    
    
    