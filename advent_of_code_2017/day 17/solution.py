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
# %%
import os
import re
import numpy as np

try:
	os.chdir(os.path.join(os.getcwd(), 'day 17'))
	print(os.getcwd())
except:
	pass


# %%

step = 369
buffer = [0]
pos = 0
for p in range(1,2018):
    if p%1000000==0: print(p)
    pos = (pos+step)%len(buffer)+1
    buffer.insert(pos,p)
buffer[buffer.index(2017)+1]

# %%
# part 2
step = 369
buffer = 1
pos = 0
res = []
for p in range(1,50000000):
    if p%1000000==0: print(p)
    pos = (pos+step)%buffer+1
    if pos == 1 : 
        print(p)
        res.append(p)
    buffer+=1
res


# %%
# found this one from the megathread on reddit
from collections import deque
step = 369
spinlock = deque([0])

for i in range(1, 2018):
    spinlock.rotate(-step)
    spinlock.append(i)

print(spinlock[0])