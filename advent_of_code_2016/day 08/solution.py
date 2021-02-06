#%%
# always check the input carefully after opening and splitting
# split r and c indices for simplicity (instead of combining them into a tuple)
# when using re, be sure to thing if greedy or nongreedy parsing is necessary
# don't use re when split() suffices, whitespaces can be casted to int
# make sure to experiment with one item from a list instead of and immediate for loop
# when there is a clear test case available, test it!
# scan over the input a bit more carefully, it may be different than the test examples
# when plotting, use plt.imshow (not plt.show)
# %%

import re
import numpy as np
import matplotlib.pyplot as plt

f = open('input.txt','r')
lines = [line.rstrip() for line in f]
print(f'len lines {len(lines)} first item {lines[0]}')

# %%
grid = np.zeros((6,50))
for l in lines:
    if l[:3]=='rec':
        c,r = map(int,(re.findall('(\d+)x(\d+)',l)[0]))
        grid[:r,:c]=1
    elif l[:9]== 'rotate co':
        c,n = map(int,(re.findall('(\d+) by (\d+)',l)[0]))
        grid[:,c] = np.roll(grid[:,c],n,axis=0)
    elif l[:9]== 'rotate ro':
        r,n = map(int,(re.findall('(\d+) by (\d+)',l)[0]))
        grid[r] = np.roll(grid[r],n,axis=0)
    else: print('problem')
plt.imshow(grid)
np.sum(grid)

# %%
