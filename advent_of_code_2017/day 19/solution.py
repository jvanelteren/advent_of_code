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

# %%
import os
import numpy as np
try:
	os.chdir(os.path.join(os.getcwd(), 'day 19'))
	print(os.getcwd())
except:
	pass

# %%
f = open('input.txt','r')
lines = [list(line) for line in f]

grid = np.array(lines)
grid.shape
start = (0,19)
grid[start]

dc = 0
dr = 1
res = []
count = 0
while True:
    count +=1
    if grid[start].isupper(): 
        res.append(grid[start])
        if grid[start] == 'P':
            print(count)
            break
    if grid[start]=='+':
        if dc == 1 or dc == -1:
            dc = 0
            if grid[start[0]+1,start[1]]=='|':
                dr = 1
            else:
                dr = -1
        elif dr == 1 or dr == -1:
            dr = 0
            if grid[start[0],start[1]+1]=='-':
                dc = 1
            else:
                dc = -1
    start = (start[0]+dr,start[1]+dc)

''.join(res)

# %%
