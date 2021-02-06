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
from collections import defaultdict

try:
	os.chdir(os.path.join(os.getcwd(), 'day 22'))
	print(os.getcwd())
except:
	pass
    
# %%
f = open('input.txt','r')
arr = np.array([list(line.rstrip()) for line in f])
grid = defaultdict(lambda: '.')
for i,j in np.ndenumerate(arr):
    grid[complex(i[1],-i[0])] = j # be careful numpy row becomes minus i, col becomes x

move = 0+1j
i = 0
pos = 12-12j
print(grid[pos])
infect = 0
for k in range(10000000):
    if k %1000000 == 0: print(k)
    if grid[pos]=='.': #turn left
        move *= 1j
        grid[pos]='W'
    elif grid[pos]=='#': # turn right
        move *= -1j
        grid[pos]='F'
    elif grid[pos]=='F': # reverse
        move *= -1
        grid[pos]='.'
    elif grid[pos]=='W':
        grid[pos]='#'
        infect += 1
    pos = pos+move
infect
# %%
# %%
