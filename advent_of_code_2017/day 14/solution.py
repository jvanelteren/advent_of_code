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
# %%
import os
import re
import numpy as np

try:
	os.chdir(os.path.join(os.getcwd(), 'day 14'))
	print(os.getcwd())
except:
	pass

from functools import reduce
import operator
import networkx as nx
import numpy as np

# f = open('input.txt','r').read().strip()

def gethash(f):
    lengths = [ord(l) for l in f]
    lengths += [17, 31, 73, 47, 23]
    circular = np.arange(256)
    skip = 0
    start = 0
    for r in range(64):
        for l in lengths:
            circular = np.roll(circular,-start)
            circular[:l]=circular[:l][::-1]
            circular = np.roll(circular,+start)
            start = (start + l + skip)%len(circular)
            skip +=1
    def densehash(inp):
        return (reduce(lambda a,b : operator.xor(a,b),inp))
    hashcode = ''
    for i in range(16):
        hashcode +=  hex(densehash(circular[i*16:i*16+16]))[2:].zfill(2)
    return hashcode

def getbits(inp):
    my_hexdata = inp
    scale = 16 ## equals to hexadecimal
    num_of_bits = 4
    return bin(int(my_hexdata, scale))[2:].zfill(num_of_bits)

count= 0
f = 'stpzcrnm'
for r in range(128):
    h = gethash('stpzcrnm-'+str(r))
    count+=len(''.join([getbits(b) for b in h]).replace('0',''))
count
# %%
count= 0
grid = []
f = 'stpzcrnm'
for r in range(128):
    h = gethash('stpzcrnm-'+str(r))
    grid.append(list(''.join([getbits(b) for b in h])))
    count+=len(''.join([getbits(b) for b in h]).replace('0',''))

# %%
grid = np.array(grid)
print(grid.shape)
G = nx.Graph()

for index,output in np.ndenumerate(grid):
    if output == '1':
        i,j = index[0], index[1]
        G.add_edge((i,j),(i+1,j))
        G.add_edge((i,j),(i-1,j))
        G.add_edge((i,j),(i,j+1))
        G.add_edge((i,j),(i,j-1))

for index,output in np.ndenumerate(grid):
    if output == '0':
        if G.has_node(index): G.remove_node(index)

nx.number_connected_components(G)
# %%
