#%%
# read full assignment
# think algo before implementing
# dont use a dict when you need a list
# assignment is still = and not ==
# dont use itertools when you can use np.roll
# check mathemathical functions, e.g. if the parentheses are ok
# networkx is awesome
# sometimes while true is better than just too small for loop
# networkx addes nodes when adding edge to nonexistent node
# bitwise comparison is a nice trick
# fiddling with regex can take a lot of time
# insert on a list takes too much time when done often
# check the values from a dict or list after you set them
# check the input for edge cases
# implement very carefully, e.g. >0 instead of !=0
# day 23 was reverse engineering, took a lot of time. write down states of the program before tinkering with instructions
# with a difficult problem, use the test cases first

# %%
import os
import re
import numpy as np

try:
	os.chdir(os.path.join(os.getcwd(), 'day 24'))
	print(os.getcwd())
except:
	pass

# %%
f = open('test0.txt','r')
ports = [line.rstrip().split('/') for line in f]
ports

for i in range(len(ports)):
    ports[i] = [int(ports[i][0]),int(ports[i][1])]


def findnext(left,path,search):
    poss = []
    for i in left:
        if int(i[0])==search:
            poss.append({'p': path.copy()+i,
                        'newsearch': i[1],
                        'left':left.copy()})
            poss[-1]['left'].remove(i)
        if i[1]==search and i[0]!=i[1]:
            poss.append({'p': path.copy()+i,
                        'newsearch': i[0],
                        'left':left.copy()})
            poss[-1]['left'].remove(i)
    if len(poss)==0:
        yield sum(path),len(path)
    else: 
        for p in 
        yield from [findnext(p['left'],p['p'],p['newsearch']) for p in poss]

search = 0
paths = []
res = findnext(ports.copy(),paths,0)
m = ([i[1] for i in res)])
# max([i[0] for i in res if i[1]==m])
# %%
import networkx as nx
G = nx.DiGraph()
for x,i in enumerate(ports):
    G.add_edge((x,i[0]),(x,i[1]))
    G.add_edge((x,i[1]),(x,i[0]))

    for y,j in enumerate(ports):
        if x != y:
            if i[0]==j[0]: G.add_edge((x,i[0]),(y,j[0]))
            if i[0]==j[1]: G.add_edge((x,i[0]),(y,j[1]))
            if i[1]==j[0]: G.add_edge((x,i[1]),(y,j[0]))
            if i[1]==j[1]: G.add_edge((x,i[1]),(y,j[1]))
            if i[0]==0: G.add_edge((x,i[0]),(-1,0))
            if i[1]==0: G.add_edge((x,i[1]),(-1,0))

    
# %%
largest = 0
a = (nx.all_simple_paths(G,(-1,0),(1,ports[1][0])))
while a:
    b = next(a)
    if sum([i[1] for i in b])> largest:
        largest = sum([i[1] for i in b])
largest


# for x,i in enumerate(ports):
#     nx.all_simple_paths(G,(-1,0),(x,i[0]))
#     nx.all_simple_paths(G,(-1,0),(x,i[0]))

# %%

from collections import defaultdict 
def gen_bridges(bridge, components):
    bridge = bridge or [(0, 0)]
    cur = bridge[-1][1]
    for b in components[cur]:
        if not ((cur, b) in bridge or (b, cur) in bridge):
            new = bridge+[(cur, b)]
            yield new
            yield from gen_bridges(new, components)

def parse_components(input):
    components = defaultdict(set)
    for l in input.strip().splitlines():
        a, b = [int(x) for x in l.split('/')]
        components[a].add(b)
        components[b].add(a)
    return components

def solve(input):
    components = parse_components(input)
    mx = []
    for bridge in gen_bridges(None, components):
        mx.append((len(bridge), sum(a+b for a, b in bridge)))
    return mx

input = open('input.txt','r').read()
solution = solve(input)
part1 = sorted(solution, key=lambda x: x[1])[-1][1]
part2 = sorted(solution)[-1][1]

# %%
