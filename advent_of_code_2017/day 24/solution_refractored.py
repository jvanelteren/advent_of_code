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
# with a difficult problem, use the test cases first. and use a generator with a recursive function

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
with open('test0.txt','r') as f:
    ports = [list(map(int,line.split('/'))) for line in f]

def findnext(left,path,search):
    poss = []
    for i in left:
        if int(i[0])==search:
            poss.append({'p': path+i,
                        'newsearch': i[1],
                        'left':left})
            poss[-1]['left'].remove(i)
        if i[1]==search and i[0]!=i[1]:
            poss.append({'p': path+i,
                        'newsearch': i[0],
                        'left':left})
            poss[-1]['left'].remove(i)
    if len(poss)==0:
        yield sum(path),len(path)
    else: 
        for p in poss:
            yield from findnext(p['left'],p['p'],p['newsearch'])
search = 0
paths = []
res = list(findnext(ports.copy(),paths,0))
strongest = max([i[0] for i in res])
longest = max([i[1] for i in res])
print(strongest)
print(max([i[0] for i in res if i[1]==longest]))
# %%
with open('test0.txt','r') as f:
    ports = [list(map(int,line.split('/'))) for line in f]
ports
# %%
import aoc
with open('test0.txt','r') as f:
    ports = [aoc.to_int((line.split('/'))) for line in f]
ports
# %%
