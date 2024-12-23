#!/bin/python
from copy import deepcopy
from dataclasses import dataclass
import os

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
        global lines
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


def findall(c):
    y = 0
    pp = []
    for l in lines:
        p = [i for i in range(len(l)) if l.startswith(c, i)]
        for x in p:
            pp.append(Coord(x,y))
        y+=1
    return pp

def put_ants(p, pp):
    global ant
    for a in pp:
        d = a.diff(p)
        p1 = a.add(d)
        p2 = p.sub(d)
        if p1:
            ant[p1.y][p1.x]='#'
        if p2:
            ant[p2.y][p2.x]='#'

dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")
lines = []
ant=[]
for l in f.readlines():
    lines.append(l.strip())
    ant.append(list(l.strip()))
    
    
sum = 0
for c in range(0x30, 0x7b):
    c = chr(c)
    if c.isdigit() or c.isalpha():
        pp = findall(c)
        if len(pp) > 0:
            print(c, pp)
            for i,p in enumerate(pp):
                put_ants(p, pp[i+1:])
print(sum)
for l in ant:
    for c in l:
        if c=='#':
            sum +=1
        print(end=c)
    print()
print(sum)
    
    