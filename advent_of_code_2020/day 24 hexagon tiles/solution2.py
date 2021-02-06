# set implementation maybe better keeping track of black tiles

# %%

import re

f=open('test0.txt')
lines = [line.rstrip('\n') for line in f]

delta = {
    'e':(0,2),
    'se':(1,1),
    'sw':(1,-1),
    'w':(0,-2),
    'nw':(-1,-1),
    'ne':(-1,1)}

blacks = set()

for line in lines:
    instructions = re.findall(r'(sw|se|e|w|ne|nw)',line)
    R = 0
    C = 0

    for ins in instructions:
        DR, DC = delta[ins]
        R += DR
        C += DC

    if (R,C) in blacks:
        blacks.remove((R,C))
    else:
        blacks.add((R,C))

print(len(blacks))
#%%
# part 2
def getneigh(coor):
    R, C = coor
    return {(R+dr, C+dc) for dr,dc in delta.values()}

def count_neigh(coor):
    return len(getneigh(coor) & blacks)

for i in range(100):
    neighbors = set().union(*(getneigh(b) for b in blacks))
    neighbors -= blacks # only white neighbors
    newblacks = {n for n in neighbors if count_neigh(n) == 2}
    blacks = {b for b in blacks if 0 < count_neigh(b) <= 2} | newblacks

print(len(blacks))

# %%
