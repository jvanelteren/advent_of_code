# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% De werkmap van de werkruimte root naar de ipynb-bestandslocatie veranderen. Schakel deze toevoeging uit met de instelling DataScience.changeDirOnImportExport
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'day 03'))
	print(os.getcwd())
except:
	pass

# %%
import numpy as np

#os.chdir(_dh[1])
f=open('test0.txt') #not with read because thats probably the whole file
lines = [line.rstrip('\n') for line in f]


# %%
def conv_coordinate(instruction):
    if instruction[0] == 'U': return (instruction[1],0)
    if instruction[0] == 'D': return (-instruction[1],0)
    if instruction[0] == 'R': return (0,instruction[1])
    if instruction[0] == 'L': return (0,-instruction[1])

wires = [l.split(',') for l in lines]
wires[0] = [conv_coordinate((s[0],int(s[1:]))) for s in wires[0]]
wires[1] = [conv_coordinate((s[0],int(s[1:]))) for s in wires[1]]


# %%
def counter(wire): # to explore extremes of the grid
    lr = np.array([0,0])
    ud = np.array([0,0])
    point=np.array([0,0])
    for m in wire:
        point = point+m
        if point[1] < lr[0]: lr[0] = point[1]
        if point[1] > lr[1]: lr[1] = point[1]
        if point[0] < ud[0]: ud[0] = point[0]
        if point[0] > ud[1]: ud[1] = point[0]
    return lr,ud 


# %%
[counter(w) for w in wires][0] 


# %%
import copy
def draw_wire(grid, wire,point):
    # print(wire)
    for s in wire:
        # print((grid))
        new = point + s
        # print(point,new)
        # print(slice(min(point[0],new[0]),max(point[0],new[0])+1),slice(min(point[1],new[1]),max(point[1],new[1])+1))
        grid[min(point[0],new[0]):max(point[0],new[0])+1,min(point[1],new[1]):max(point[1],new[1])+1]=1
        point = copy.deepcopy(new)
    return grid


# %%
coor = [counter(w) for w in wires] 
mind = min(coor[0][1][0],coor[1][1][0])-2
maxu = max(coor[0][1][1],coor[1][1][1])+2
minl = min(coor[0][0][0],coor[1][0][0])-2
maxr = max(coor[0][0][1],coor[1][0][1])+2
print('minmax',mind,maxu,minl,maxr)

start = np.array([-mind-1,-minl-1])

grids = [draw_wire(np.zeros((maxu-mind,maxr-minl)),w,start) for w in wires]


# %%
for g in grids:
    print(np.flip(g,axis=0),g.shape)


# %%
def manhattan(x,y):
    return abs(x[0]-y[0])+abs(x[1]-y[1])


# %%
totalgrid = np.multiply(grids[0],grids[1])
cuts = np.argwhere(totalgrid==1)
distances = [manhattan(start,c) for c in cuts]


# %%
cuts


# %%
len(distances)


# %%
totalgrid


# %%
totalgrid[1:9,1:2]= range(10,18)


# %%
totalgrid[1:2,1:6].shape


# %%

len(range(10,15))


# %%
def draw_count_wire(grid, wire,point):
    count = 0
    for s in wire:
        print((grid))
        new = point + s
        distance = manhattan(point,new)
        print(f'c{count},d{distance}')
        # print(point,new)
        # print(min(point[0],new[0]):max(point[0],new[0])+1,min(point[1],new[1]):max(point[1],new[1])+1)
        grid[min(point[0],new[0]):max(point[0],new[0])+1,min(point[1],new[1]):max(point[1],new[1])+1]=range(count,count+distance+1)
        count += distance
        point = copy.deepcopy(new)
    return grid


# %%
countgrids = [draw_count_wire(np.zeros((maxu-mind,maxr-minl)),w,start) for w in wires]


# %%



# %%


