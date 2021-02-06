#%%
# read full assignment
# think algo before implementing
# dont use a dict when you need a list
# assignment is still = and not ==
# dont use itertools when you can use np.roll
# check mathemathical functions if the parentheses are ok
# networkx is awesome
# %%
import os
import networkx as nx
import re

try:
	os.chdir(os.path.join(os.getcwd(), 'day 12'))
	print(os.getcwd())
except:
	pass

f = open('input.txt','r')
code =  [re.findall('(.+) <-> (.+)',line)[0] for line in f]
pipes = {line[0]:line[1].split(', ') for line in code}

g = nx.Graph()
g.add_nodes_from(pipes)
for k,v in pipes.items():
    for c in v:
       g.add_edge(k,c)

# part 1
len(nx.descendants(g, '0'))

# %%
#part 2
nx.number_connected_components(g)
