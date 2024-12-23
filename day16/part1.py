#!/bin/python
from copy import deepcopy
from dataclasses import dataclass
import os
import sys

@dataclass
class Coord:
    x: int = 0
    y: int = 0
    maxx = 0xffffffff
    maxy = 0xffffffff

    def __init__(self,x,y):
        global lines
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

def pos_is(pos,c):
    return lines[pos.y][pos.x] == c
BLUE = '\033[94m'
CYAN = '\033[96m'
GREEN = '\033[92m'
ORANGE = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def find_path(pos,dir, path, points):
    global scores
    if pos_is(pos,'E'):
        global fi
        print("FOUND END", fi, points)
        scores.append(points)
        # print(scores)
        pa=deepcopy(lines)
        for p in path:
            pa[p[0].y][p[0].x] = f"{RED}{BOLD}{p[1]}{ENDC}"
        f = open(f"end{fi}",'w')
        for l in pa:
            f.write("".join(l))
            f.write("\n")
        f.close()
        fi+=1

        return points
    if points > seen[pos.y][pos.x]:
        return 0xffffffffff
    else:
        points_to_end=0xffffffff
        seen[pos.y][pos.x] = points
        next = pos.add(DIRS[dir])
        if not pos_is(next,'#'):
            p=find_path(next, dir, path+[(pos, DIRC[dir])], points+1)
            points_to_end=min(p, points_to_end)
                    
        dir = (dir + 1)%4              
        next = pos.add(DIRS[dir])
        if not pos_is(next,'#'):
            p=find_path(next, dir, path+[(pos, '*')], points+1001)
            points_to_end=min(p, points_to_end)
        
        dir = (dir + 2)%4              
        next = pos.add(DIRS[dir])
        if not pos_is(next,'#'):
            p=find_path(next, dir, path+[(pos, '*')], points+1001)
            points_to_end=min(p, points_to_end)

        to_end[pos.y][pos.x] = points_to_end
        return points_to_end
    
dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")
lines = []
seen=[]
to_end=[]
y = 0
for l in f.readlines():
    lines.append(list(l.strip()))
    seen.append([0xffffffff]*len(lines[0]))
    to_end.append([0xffffffff]*len(lines[0]))
    x = l.find('S')
    if x >=0:
        pos=Coord(x, y)
    y+=1

pos.maxy=len(lines)-1

DIRS=[
    Coord(1,0),
    Coord(0,1),
    Coord(-1,0),
    Coord(0,-1)
]
DIRC=['>','v','<','^']
fi=0
dir=0
scores=[]
path=[]
sys.setrecursionlimit(15000)
find_path(pos, dir, path, 0) 

sum = 0
m=0xffffffff
for s in scores:
    m = min(m,s)
    
print(scores)
print(m)
    
    
    