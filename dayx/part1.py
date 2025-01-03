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

dir = os.path.dirname(__file__)
f = open(dir+"/input.txt")
lines = []
for l in f.readlines():
    lines.append(l.strip())
    
    
sum = 0
for l in lines:
    pass
print(sum)
    
    
    