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
    if l == "":
         continue
    if "|" in l:
        ru.append(l)
    else:
        s = l.split(",")
        sorted = False
        n = 0
        while not sorted:
            n+=1
            sorted = True
            for i in range(len(s)-1):
                if f"{s[i+1]}|{s[i]}" in ru:
                    t = s[i]    
                    s[i]=s[i+1]
                    s[i+1] = t
                    sorted = False
        if n != 1:
            print(s)
            m = (len(s)-1)/2
            sum += int(s[int(m)])

print(sum)
    
    
    