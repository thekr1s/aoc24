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

@dataclass
class Coord:
    x: int = 0
    y: int = 0
    maxx = 0xffffffff
    maxy = 0xffffffff

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

def string_to_ints(str, separator):
    s = str.strip().split(separator)
    a = []
    for n in s:
        a.append(int(n.strip()))
    return a


VECS = [
    [Coord(1,1), Coord(-1,-1)],
    [Coord(1,-1), Coord(-1,1)]
]

def is_mas(pos: Coord, vecs:[Coord,Coord]): # type: ignore
    p1 = pos.add(vecs[0])
    p2 = pos.add(vecs[1])
    c1 = lines[p1.y][p1.x]
    c2 = lines[p2.y][p2.x]
    if (c1=="M" and c2=="S") or (c1=="S" and c2=="M"):
        return True
    return False

dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")
lines = []
for l in f.readlines():
    lines.append(l.strip())
    
    
sum = 0
pos = Coord(0,0)
pos.set_max(len(lines[0])-1, len(lines)-1)

for x in range(1,pos.maxx):
    for y in range(1,pos.maxy):
        pos.x=x
        pos.y=y
        if lines[pos.y][pos.x] == 'A':
            if is_mas(pos, VECS[0]):
                if is_mas(pos, VECS[1]):
                    sum+=1
        


print(sum)
    
    
    