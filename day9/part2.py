#!/bin/python
from dataclasses import dataclass
import os

def string_to_ints(str, separator):
    s = str.strip().split(separator)
    a = []
    for n in s:
        a.append(int(n.strip()))
    return a

def get_size(pos):
    global disk
    l = 0
    while disk[pos + l] == disk[pos]:
        l+=1
    return l

def get_size_rev(pos):
    global disk
    l = 0
    while disk[pos - l] == disk[pos]:
        l+=1
    return l
 
dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")
lines = []
disk=[]
for l in f.readlines():
    l=l.strip()
    lines.append(l)


file=True
id = 0
l=lines[0]
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

print()


i=len(disk)-1
while i >0:
    print(i)
    s = get_size_rev(i)
    if disk[i]!= '.':
        j = 0
        while j < (i-s):
            ss = get_size(j)
            if ss >= s and disk[j] == '.':
                for k in range(s):
                    disk[j+k]=disk[i-k]
                    disk[i-k]='.'
                break
            else:
                j += ss

    i -= s;


sum = 0
for i, e in enumerate(disk):
    print(end=str(e))
    if e != '.':
        sum += e*i



print()
for l in lines:
    pass
print(sum)
    
    
    