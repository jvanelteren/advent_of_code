#%%
# always check the input carefully after opening and splitting
# split r and c indices for simplicity (instead of combining them into a tuple)
# when using re, be sure to thing if greedy or nongreedy parsing is necessary
# don't use re when split() suffices, whitespaces can be casted to int
# make sure to experiment with one item from a list instead of and immediate for loop
# !when there is a clear test case available, test it!
# scan over the input a bit more carefully, it may be different than the test examples
# when plotting, use plt.imshow (not plt.show)
# i should look into itertools more
# when refractoring a test case into the real code, check the indices are not hardcoded!
# use better descriptive names. also unpack if it makes code more readable for example in list of tuples
# with regex you can numbers pretty easily in a line. and -? to add possible negatives
# sometimes its easier to brute force bfs than to figure out an insane algo yourself
# at beginning look at example first and highlighted texts
# use the easiest way to calculate solution (is set A is asked, dont calc set total - set B)
# when defining multiple functions, but an assert testcase below it that closely resembles input
# use a class with __hash__ to store mutable objects
# with assembly analysis make sure to print registers at important jump points
# don't implement an algo if you are pretty sure it isnt going to work

# %%
f = open('input.txt','r')
lines = [list(line.rstrip()) for line in f]
print(f'len lines {len(lines)} first item {lines[0]}')

import numpy as np
grid = np.array(lines)
grid


import networkx as nx
G = nx.Graph()

for cell,value in np.ndenumerate(grid):
    G.add_node(cell)
for cell,value in np.ndenumerate(grid):

    if value != '#':
        for delta in [[0,1],[1,0],[0,-1],[-1,0]]:
            r2 = cell[0]+delta[0]
            c2 = cell[1]+delta[1]
            if 0<= r2 < grid.shape[0] and 0<= c2 < grid.shape[1] and grid[r2,c2]!='#':
                G.add_edge(cell,(r2,c2)) 

# %%
poi = {}
for cell,value in np.ndenumerate(grid):
    if value.isdigit(): poi[cell] = value
start = [k for k,v in poi.items() if v == '0'][0]
total_dis = 0

for fromcell in poi:
    distances = {}
    for tocell in poi:
        if fromcell != tocell:
            distances[tocell]= nx.shortest_path_length(G, source=fromcell, target=tocell)
    poi[fromcell]=distances
poi
best = 9999
from itertools import permutations
for p in permutations(poi,len(poi)):
    if p[0]== start:
        dis = 0
        p = list(p)
        p.append(start)
        for i,j in zip(p,p[1:]):
            dis+=poi[i][j]
        if dis < best: best = dis
best
