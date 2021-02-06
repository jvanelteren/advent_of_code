#%%
# always check the input carefully after opening and splitting
# split r and c indices for simplicity (instead of combining them into a tuple)
# when using re, be sure to thing if greedy or nongreedy parsing is necessary
# don't use re when split() suffices, whitespaces can be casted to int
# make sure to experiment with one item from a list instead of and immediate for loop
# %%
from collections import Counter

f = open('input.txt','r')
lines = [line.rstrip() for line in f]
print(f'len lines {len(lines)} first item {lines[0]}')
part1 = []
part2 = []
for i in range(len(lines[0])):
    part1.append(Counter(''.join([l[i] for l in lines])).most_common(1)[0])
    part2.append(Counter(''.join([l[i] for l in lines])).most_common()[-1])
print(''.join([r[0] for r in part1]))
print(''.join([r[0] for r in part2]))
# %%
# alternative

import numpy as np
grid = np.array(lines)
def find_most(i):
    return Counter(grid[:,i]).most_common(1)[0][0] 
def find_least(i):
    return Counter(grid[:,i]).most_common()[-1][0] 
print(''.join(find_most(i) for i in range(grid.shape[1])))
print(''.join(find_least(i) for i in range(grid.shape[1])))