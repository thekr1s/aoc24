#!/bin/python
from dataclasses import dataclass
import os

def string_to_ints(str, separator):
    s = str.strip().split(separator)
    a = []
    for n in s:
        a.append(int(n.strip()))
    return a        

def calc(exp, val, vals):
    global sum
    if len(vals) > 0:
        v = val*vals[0]
        if calc(exp, v, vals[1:]):
            return True
        v = val+vals[0]
        if calc(exp, v, vals[1:]):
            return True
        v = int(str(val)+str(vals[0]))
        if calc(exp, v, vals[1:]):
            return True

        return False
    else:
        if val == exp:
            print(sum, val)
            sum+=val
            return True
        else:
            return False
dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")
lines = []
for l in f.readlines():
    lines.append(l.strip())
    

     

sum = 0
for l in lines:
    t,n = l.split(":")
    exp = int(t)
    n=string_to_ints(n," ")
    calc(exp, n[0], n[1:])


print(sum)
    
    
    