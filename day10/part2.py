#!/bin/python
from copy import deepcopy
from dataclasses import dataclass
import os

lines = None
def string_to_ints(str, separator):
    s = str.strip().split(separator)
    a = []
    for n in s:
        a.append(int(n.strip()))
    return a

@dataclass
class Coord:
    x: int = 0
    y: int = 0
    maxx = 0xffffffff
    maxy = 0xffffffff

    def __init__(self,x,y):
        if lines:
            self.maxx= len(lines[0])-1
            self.maxy= len(lines)-1
        self.x = x
        self.y = y

    def set_max(self, x,y):
        self.maxx = x
        self.maxy = y

    def add(self, c):
        cc = deepcopy(self)

        cc.x += c.x
        cc.y += c.y

        if cc.x < 0 or cc.y<0:
            return None
        if cc.x > cc.maxx or cc.y>cc.maxy:
            return None
        return cc;

    def sub(self, c):
        cc = deepcopy(self)

        cc.x -= c.x
        cc.y -= c.y

        if cc.x < 0 or cc.y<0:
            return None
        if cc.x > cc.maxx or cc.y>cc.maxy:
            return None
        return cc;

    def diff(self, c):
        cc = deepcopy(self)

        cc.x -= c.x
        cc.y -= c.y

        return cc;

    def get(self):
        c = lines[self.y][self.x]
        if c == '.':
            return -1
        else:
            return int(c)

DIRS=[
    Coord(1,0),
    Coord(0,1),
    Coord(-1,0),
    Coord(0,-1)
]

count = 0
found=[]
def findpath(path):
    global count
    p = path[len(path)-1]
    v = p.get()
    if v == -1:
        return
    for d in DIRS:
        n = p.add(d)
        if n and n.get() != -1 and not n in path and n.get()-v == 1:
            if n.get() == 9:
                count +=1
                found.append(n)
            else:
                findpath(path + [n])

dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")
lines = []
for l in f.readlines():
    lines.append(l.strip())
sum = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        p = Coord(x,y)
        if p.get() == 0:
            count = 0
            found=[]
            findpath([p])
            print(p, count)
            sum += count

print(sum)
    
    
    