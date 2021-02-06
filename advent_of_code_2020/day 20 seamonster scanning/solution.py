# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
from collections import Counter, defaultdict, namedtuple, deque
from math import gcd, ceil
import re
import networkx as nx
from dataclasses import dataclass
import itertools
import aoc
from matplotlib import pyplot as plt
import string
# plt.imshow(pic)

from collections import deque
def bfs(connections, start, goal=None):
    """
    Requires a connections dict with tuples with neighbors per node.
    Or a connections function returning neighbors per node

    Returns
    if goal == None:    return dict of locations with neighbor closest to start
    elif goal found:    returns path to goal
    else:               returns False
    """
    seen = set() # the locations that have been explored
    frontier = deque([start]) # the locations that still need to be visited
    # paths = {start: [start]}
    isfunction = callable(connections)
    parents = {start: None}
    counter = 0

    def get_path(parents,start,goal):
        # print(start,goals)
        cur = goal
        path = [cur]
        while cur != start:
            cur = parents[cur]
            path.append(cur)
        path.reverse()
        return path

    while frontier:
        counter +=1
        search = frontier.popleft()
        if counter % 500 == 0: print(len(frontier))
        # if counter % 500 == 0: print(search)
        if isfunction: neighbors = connections(search)
        else: neighbors = connections.get(search,None)
        if neighbors:
            for n in neighbors:
                if n not in seen:

                    seen.add(n)
                    frontier.append(n)
                    # paths[n] = paths[search]+[n]
                    parents[n]= search
                    if goal and n[0] == goal:
                        # print('goal found')
                        return n
                        # return paths[goal],parents
        seen.add(search)
    if goal: return False
    else: return parents
# %%
def get_orients(grid):
    res = []
    grid = np.array(grid)
    for _ in range(2):
        for j in range(4):
            res.append(np.rot90(grid,j).tolist())
        grid = np.flip(grid, axis = 0) # the axis does not matter
    return res
 


# %%
f =  open('input.txt').read()
lines = [l.rstrip('\n') for l in f.split('\n\n')]

maxnum = int(len(lines)**0.5)
tiles ={}
for tile in lines:
    id, grid = tile.split(':\n')
    _, idname = id.split()
    idname = int(idname)
    grid = [list(line)for line in grid.split('\n')]
    tiles[idname] = get_orients(grid)

def findnext(tofill):
    r, c = tofill
    if c == maxnum - 1:
        return (r+1, 0)
    else:
        return (r, c+1)


# %%

def fits(assignments, tofill, cand_grid, debug=False):
    valid = True
    if tofill == (0,0): return True
    for dr,dc in ((-1,0), (0,-1)):
        r = tofill[0] + dr
        c = tofill[1] + dc

        if 0 <= r <= maxnum and 0 <= c <=maxnum:
            if debug: print('checking with',r,c)

            if dr == -1:
                first = cand_grid
                second_id, second_orient = assignments[(r,c)] # has number and orient
                second = tiles[second_id][second_orient]
                if first[0] != second[-1]:
                    if debug: print('dr false' + str(first[0]) + str(first[-1]))
                    return False

            elif dc == -1:
                first = cand_grid
                second_id, second_orient = assignments[(r,c)] # has number and orient
                second = tiles[second_id][second_orient]
                for i in range(10):
                    if debug: print(first[i][0] + second[i][-1])
                    if first[i][0] != second[i][-1]:
                        if debug: print('dc false' + str(second))
                        if debug: print('dc false' + str(first))
                        return False
    return valid


# %%
count = 0
def get_neigh(state):
    neigh = []
    tofill, assignments = state
    global count
    if tofill == (0,1): count+=1
    assignments = eval(assignments)
    assigned = [i[0] for i in assignments.values() if i]
    for cand_id in tiles: # loop through all tiles
        if cand_id not in assigned:
            for orientation in range(0,8): # and per tile, through all orientations
                cand_grid = tiles[cand_id][orientation]
                if fits(assignments, tofill, cand_grid):
                    nexttofill = findnext(tofill)
                    nextstate = assignments.copy()
                    nextstate[tofill] = (cand_id, orientation)
                    neigh.append((nexttofill, str(nextstate)))
    return neigh

state = ((0,0), str({(i,j): None for i in range(maxnum) for j in range(maxnum)}))
ans = bfs(get_neigh, state, (maxnum,0))


# %%
maxval = maxnum-1
answer[0,maxval][0]*answer[maxval,0][0] * answer[0,0][0] * answer[maxval,maxval][0]


# %%
# # saving something as pickle file
# import pickle
# with open('dict', 'wb') as handle:
#     pickle.dump(answer, handle, protocol=pickle.HIGHEST_PROTOCOL)
# # opening pickle file
import pickle
f = open("dict","rb")
answer = pickle.load(f)
answer

# part 2
# %%
def remove_pad(num, orient):
    grid = tiles[num][orient]
    arr = np.array(grid)
    arr = arr[1:-1,1:-1]
    return arr

output = []
for r in range(maxnum):
    col = []
    for c in range(maxnum):
        index = r*maxnum+c
        num, orient = list(answer.values())[index]
        print (r,c,index, num, orient)
        col.append(remove_pad(num,orient))
        if index == 0:
            print(col[0])
    output.append(np.hstack(col))
sea = np.vstack(output)
sea.shape

# seas = [remove_pad(num, orient) for num, orient in answer.values()]


# %%
f=open('monster.txt')
monster = [list(line.rstrip('\n')) for line in f]
for r in range(len(monster)):
    for c in range(len(monster[0])):
        if monster[r][c]==' ':monster[r][c]=False
        if monster[r][c]=='#':monster[r][c]=True
monster = np.array(monster)


ans = 0
m = monster
coor = {}
for index, s in enumerate(seas):
    sea = np.array(s)
    for r in range(sea.shape[0]-m.shape[0]+1):
        for c in range(sea.shape[1]-m.shape[1]+1):
            if not '.' in sea[r:r+m.shape[0],c:c+m.shape[1]][m]:
                print('foundm', index, r, c)
                ans +=1

