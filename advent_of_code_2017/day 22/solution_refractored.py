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
# pay attention when coding logic such as go left and go right with drs dcs


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
    
# %%
f = open('input.txt','r')
grid = np.array([list(line.rstrip()) for line in f])
grid.shape

drs = [-1,0,1,0]
dcs = [0,1,0,-1]
i = 0
pos = (1012,1012)
grid = np.pad(grid, 1000, mode='constant',constant_values = '.')
infect = 0
for k in range(10000000):
    if k %1000000 == 0: print(k)
    if grid[pos]=='.': #turn left
        i=(i-1)%len(drs)
        grid[pos]='W'
    elif grid[pos]=='#': # turn right
        i=(i+1)%len(drs)
        grid[pos]='F'
    elif grid[pos]=='F': # reverse
        i=(i+2)%len(drs)
        grid[pos]='.'
    elif grid[pos]=='W':
        grid[pos]='#'
        infect += 1
    pos = (pos[0]+drs[i],pos[1]+dcs[i])
infect
# %%
