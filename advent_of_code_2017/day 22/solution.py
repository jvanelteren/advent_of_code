#%%
# read full assignment
# think algo before implementing
# dont use a dict when you need a list
# assignment is still = and not ==
# dont use itertools when you can use np.roll
# check mathemathical functions if the parentheses are ok
# networkx is awesome
# sometimes while true is better than just too small for loop
# networkx addes nodes when adding edge to nonexistent node
# bitwise comparison is a nice trick
# fiddling with regex can take a lot of time
# insert on a list takes too much time when done often
# check the values from a dict or list after you set them
# check the input for edge cases
# be careful with multiple if statements. are they all if or elif?
# dict of dataclass works better than dict of dicts
# convolutions are not so easy to implement
# pay attention when coding logic such as go left and go right with dr dc


# %%
import os
import numpy as np
from dataclasses import dataclass
import re

try:
	os.chdir(os.path.join(os.getcwd(), 'day 22'))
	print(os.getcwd())
except:
	pass
    
@dataclass
class Pos:
    pos:list
    vel:list
    acc:list

# %%
f = open('input.txt','r')
grid = np.array([list(line.rstrip()) for line in f])
grid.shape


def step(grid,pos,dr,dc):

    infect = 0
    if grid[pos]=='.': #turn left
        if dr==1:
            dr = 0
            dc = 1
        elif dr==-1:
            dr = 0
            dc = -1
        elif dc==1:
            dc = 0
            dr = -1
        elif dc==-1:
            dc = 0
            dr = 1
    elif grid[pos]=='#': # turn right
        if dr==1:
            dr = 0
            dc = -1
        elif dr==-1:
            dr = 0
            dc = 1
        elif dc==1:
            dc = 0
            dr = 1
        elif dc==-1:
            dc = 0
            dr = -1
    elif grid[pos]=='F': # reverse
        dc = -dc
        dr = -dr
    # print('grid is ',grid[pos])
    if grid[pos]=='.':grid[pos]='W'
    elif grid[pos]=='W':
        grid[pos]='#'
        infect = 1
    elif grid[pos]=='#':grid[pos]='F'
    elif grid[pos]=='F':grid[pos]='.'
    # print('grid is ',grid[pos],'\n')
    
    pos = (pos[0]+dr,pos[1]+dc)
    return grid,pos, dr,dc, infect

dr = -1
dc = 0
pos = (1012,1012)
inf = 0
grid = np.pad(grid, 1000, mode='constant',constant_values = '.')
print(grid.shape,grid[pos])

# %%
for i in range(10000000):
    if i %100000 == 0: print(i)
    grid,pos,dr,dc,c = step(grid,pos,dr,dc)
    # print(pos,dr,dc)
    inf += c
grid[8:15,8:15],inf

# %%
