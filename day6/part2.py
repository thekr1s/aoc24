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

def get_c(c: Coord):
    global lines
    return lines[c.y][c.x]

def set_c(c: Coord, s):
    global lines
    lines[c.y][c.x]=s

VECS = [
    Coord(0,1),
    Coord(1,0),
    Coord(0,-1),
    Coord(-1,0),
]

def walk_path(pos):
    global lines
    end = False
    dir=2
    path=[]
    while not end:
        next = pos.add(VECS[dir])
        # set_c(pos,'X')        
        if next == None:
            break
        if get_c(next) == "#":
            if get_c(pos) == 'o':
                print("been here before")
                return None
            set_c(pos,'o')        
            dir -=1
            if dir < 0: 
                dir = 3
        pos = pos.add(VECS[dir])
        if not pos in path:
            path.append(pos)

    return path


dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")
lines = []
y = 0
for l in f.readlines():
    l = l.strip()
    x = l.find("^")
    if x != -1:
        startpos=Coord(x,y)
    y+=1
    lines.append(list(l))
    
    
startpos.maxx=len(lines[0])-1
startpos.maxy=len(lines)-1
lines_org=deepcopy(lines)

pos=deepcopy(startpos)
lines= deepcopy(lines_org)
path= walk_path(pos)

print(startpos, len(path))



count = 0
sum = 0
for p in path:
    print(p, count)
    count +=1
    pos=deepcopy(startpos)
    lines=deepcopy(lines_org)
    set_c(p, "#")

    if walk_path(pos) == None:
        sum +=1

print(pos, sum)
    
    
    