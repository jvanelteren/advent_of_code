
#%%

input = 312051

total = 1
start = 1
for x in range(1,1000):
    start += 2
    total += start*2 + (start-2)*2
    if total >= input: 
        print(start,start-2)
        break
print (total,start,x) 

#compute number of items in new circle
#if total amount >= input

# %%

#%%
todo = total - input
todo -= 558
todo

# %%
558/2

# %%
279-128

# %%
151+279
# %%
# part 2 actually pretty nice
import numpy as np

def run_part_2():
    grid = np.zeros(shape=(50,50))
    grid[25,25] = 1 
    grid[25,26] = 1 
    grid[24,26] = 2 

    coor = (24,26)
    dr = [0,1,0,-1]
    dc = [-1,0,1,0]
    toadd = 2
    delta_toadd = [0,1,0,1]
    for _ in range(10):
        for i in range(4):
            # print('i',i,'toadd',toadd)
            for appending in range(toadd):
                coor = (coor[0]+dr[i],coor[1]+dc[i])
                grid[coor]= np.sum(grid[coor[0]-1:coor[0]+2,coor[1]-1:coor[1]+2])
                print(grid[coor])
                if grid[coor]>input:return grid[coor]
            toadd+=delta_toadd[i]
print(run_part_2())

# %%
# from reddit nice solution for part 2
from itertools import count
# used a dictionary for the values
# used an iterator with steps of 2
#
def sum_spiral():
    a, i, j = {(0,0) : 1}, 0, 0
    for s in count(1, 2):
        for (ds, di, dj) in [(0,1,0),(0,0,-1),(1,-1,0),(1,0,1)]:
            for _ in range(s+ds):
                i += di; j += dj
                a[i,j] = sum(a.get((k,l), 0) for k in range(i-1,i+2)
                                             for l in range(j-1,j+2))
                yield a[i,j]

def part2(n):
    for x in sum_spiral():
        if x>n: return x
part2(312051)
# %%
