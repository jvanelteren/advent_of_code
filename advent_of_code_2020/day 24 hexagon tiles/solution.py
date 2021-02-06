# set implementation maybe better keeping track of black tiles

# %%

from collections import defaultdict
import functools

f=open('input.txt')
lines = [line.rstrip('\n') for line in f]
tiles = defaultdict(int)

for line in lines:
    ins = ''
    R = 0
    C = 0
    for l in line:
        if l == 's' or l == 'n':
            ins += l
            continue
        else: 
            ins += l
        if ins =='e': 
            C += 2
        elif ins =='se':
            R += 1
            C += 1
        elif ins =='sw':
            R += 1
            C -= 1
        elif ins =='w': 
            C -= 2
        elif ins =='nw':
            R -= 1
            C -= 1
        elif ins =='ne': 
            R -= 1
            C += 1
        else: print('error')
        ins = ''

    # this operation makes a 0 into 1 and vice versa
    tiles[(R,C)] = (tiles[(R,C)] + 1) % 2 

print(sum([1 for t in tiles.values() if t == 1]))
print(len(tiles))
t2 = {k: v for k,v in tiles.items() if v ==1}
tiles = defaultdict(int)
tiles.update(t2)

print(len(tiles))
#%%
# part 2

@functools.lru_cache()
def getneigh(coor):
    R, C = coor
    # took me half an hour to find below bug, switched R and C
    # return {(R+2,C), (R-2,C), (R+1,C+1), (R+1,C-1), (R-1,C-1), (R-1,C+1)}
    return {(R,C+2),(R,C-2),(R+1,C+1),(R-1,C-1),(R+1,C-1),(R-1,C+1)}

def count_neigh(coor):
    return sum([tiles[n] for n in getneigh(coor)])

days = 100

for i in range(days):
    print (i)

    alltiles = set(tiles.keys())
    for k,v in tiles.items(): # add the neighbors
        if v == 1: # for only the black tiles
            alltiles |= getneigh(k)

    coloring = {tile: count_neigh(tile) for tile in alltiles}

    for tile, count in coloring.items():
        current = tiles[tile]
        if current == 0 and count  == 2: # white and exactly 2
            tiles[tile] = 1 # flip black
        elif current == 1 and count > 2: # >2 or exactly zero
            del tiles[tile]
        elif current == 1 and count == 0:
            del tiles[tile]
print(sum([1 for t in tiles.values() if t == 1]))
# %%

# %%
