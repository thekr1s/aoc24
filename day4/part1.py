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
        self.x += c.x
        self.y += c.y

        if self.x < 0 or self.y<0:
            return False
        if self.x > self.maxx or self.y>self.maxy:
            return False
        return True;

def string_to_ints(str, separator):
    s = str.strip().split(separator)
    a = []
    for n in s:
        a.append(int(n.strip()))
    return a


VECS = [
    Coord(1,0),
    Coord(-1,0),
    Coord(0,1),
    Coord(0,-1),
    Coord(1,1),
    Coord(1,-1),
    Coord(-1,1),
    Coord(-1,-1)
]
S="XMAS"
def find(pos: Coord, vec:Coord):
    co = deepcopy(pos)
    for c in S:
        cc=lines[co.y][co.x]
        if c == cc:
            if c == 'S':
                return True
        else:
            return False
        if not co.add(vec):
            return False


dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")
lines = []
for l in f.readlines():
    lines.append(l.strip())
    
    
sum = 0
pos = Coord(0,0)
pos.set_max(len(lines[0])-1, len(lines)-1)

for x in range(pos.maxx+1):
    for y in range(pos.maxy+1):
        pos.x=x
        pos.y=y
        if lines[pos.y][pos.x] == 'X':
            print(pos)
            for v in VECS:
                print("v:", v)
                if find(pos, v):
                    sum +=1
                    print(sum)
        


print(sum)
    
    
    