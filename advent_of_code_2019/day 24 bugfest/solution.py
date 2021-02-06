# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% De werkmap van de werkruimte root naar de ipynb-bestandslocatie veranderen. Schakel deze toevoeging uit met de instelling DataScience.changeDirOnImportExport
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'day 24'))
	print(os.getcwd())
except:
	pass
from IPython import get_ipython

import numpy as np
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class Pos:
    x:int
    y:int
    bio:int
    neigh:int
    val:int
    level:int

    @property
    def ncount(self): return len(self.neigh)
    def newval(self,state):
        bugcount = sum([state.get(n,0).val for n in self.neigh if state.get(n)])
        self.tempval = self.val
        if self.val == 0: #empty
            if bugcount == 1 or bugcount ==2:
                self.tempval = 1
        elif self.val == 1:
            if bugcount != 1:
                self.tempval = 0
    def newvalrec(self,states):
        bugcount = sum([states[l][n].val for n,l in self.neigh if states[l].get(n)])
        self.tempval = self.val
        if self.val == 0: #empty
            if bugcount == 1 or bugcount ==2:
                self.tempval = 1
        elif self.val == 1:
            if bugcount != 1:
                self.tempval = 0
        if self.x==2 and self.y ==2:
            self.tempval = 0
    def update(self): self.val = self.tempval
def neighbor2d(locations,i): #determine the neighbors from a list of locations
    res = []
    if (i[0],i[1]+1) in locations: res.append((i[0],i[1]+1))
    if (i[0],i[1]-1) in locations: res.append((i[0],i[1]-1))
    if (i[0]+1,i[1]) in locations: res.append((i[0]+1,i[1]))
    if (i[0]-1,i[1]) in locations: res.append((i[0]-1,i[1]))
    return res # list of tuples (input, neighbor)

def neighborrec(locations,i,level): #determine the neighbors from a list of locations
    res = []
    if (i[0],i[1]+1) in locations: res.append(((i[0],i[1]+1),level))
    if (i[0],i[1]-1) in locations: res.append(((i[0],i[1]-1),level))
    if (i[0]+1,i[1]) in locations: res.append(((i[0]+1,i[1]),level))
    if (i[0]-1,i[1]) in locations: res.append(((i[0]-1,i[1]),level))
    # add the outer links
    if i[0]==0:res.append(((1,2),level+1))
    if i[0]==4:res.append(((3,2),level+1))
    if i[1]==0:res.append(((2,1),level+1))
    if i[1]==4:res.append(((2,3),level+1))
        # add the inner links
    if i ==(1,2):
        for r in range(5):
            res.append(((0,r),level-1))
    if i ==(3,2):
        for r in range(5):
            res.append(((4,r),level-1))
    if i ==(2,1):
        for r in range(5):
            res.append(((r,0),level-1))
    if i ==(2,3):
        for r in range(5):
            res.append(((r,4),level-1))
    if i ==(2,2):
        res = []
    return res # list of tuples (input, neighbor)
# %%
f=open('test0.txt')
grid = np.array([list(l.strip()) for l in f])
grid[grid == '#']= 1
grid[grid == '.']= 0
state = {tuple(coor): Pos(coor[0],coor[1],0,0,int(val),0) for coor,val in np.ndenumerate(grid)}
for p in state.values():
    p.bio = pow(2,p.x*grid.shape[0]+p.y)
    p.neigh = neighbor2d(state.keys(),(p.x,p.y))

# %%
# part 1
history = []
for x in range(1005):
    for p in state.values():
        p.newval(state)
    for p in state.values():
        p.update()
    for coor,val in np.ndenumerate(grid):
        grid[coor] = state[coor].val
    checksum = [p.val for p in state.values()]
    if checksum in history:
        print(sum([p.bio*p.val for p in state.values()]))
        break
    else:
        history.append(checksum)
# %%
#part 2
f=open('input.txt')
grid = np.array([list(l.strip()) for l in f])
grid[grid == '#']= 1
grid[grid == '.']= 0
state = {tuple(coor): Pos(coor[0],coor[1],0,0,int(val),0) for coor,val in np.ndenumerate(grid)}

for p in state.values():
    p.bio = pow(2,p.x*grid.shape[0]+p.y)
states = [deepcopy(state) for _ in range(410)]
for i,s in enumerate(states):
    if i != 205:
        for p in s.values():
            p.val = 0
    if 0 < i < 408:
        for p in s.values():
            p.level = i
            p.neigh = neighborrec(state.keys(),(p.x,p.y),p.level)
for _ in range(200):
    for i,s in enumerate(states):
        if 0 < i < 408:
            for p in s.values():
                p.newvalrec(states)
    for i,s in enumerate(states):
        if 0 < i < 408:
            for p in s.values():
                p.update()

# print the sum of number of bugs
print(sum([p.val for s in states for p in s.values() ]))

# %%
