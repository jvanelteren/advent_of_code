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
# bitwise comparison is a nice trick
# fiddling with regex can take a lot of time
# insert on a list takes too much time when done often
# check the values from a dict or list after you set them
# check the input for edge cases
# be careful with multiple if statements. are they all if or elif?

# %%
import os
import numpy as np
from dataclasses import dataclass
try:
	os.chdir(os.path.join(os.getcwd(), 'day 20'))
	print(os.getcwd())
except:
	pass

part = {}
for i, line in enumerate(lines):
    p = [int(i) for i in line[0][0].split(',')]
    v = [int(i) for i in line[0][1].split(',')]
    a = [int(i) for i in line[0][2].split(',')]
    part[i]= Pos(p,v,a)

# %%
import re
f = open('input.txt','r')
lines = [re.findall('<(.*)>.*<(.*)>.*<(.*)>',line.rstrip()) for line in f]
part = {}
for i, line in enumerate(lines):
    p = line[0][0].split(',')
    v = line[0][1].split(',')
    a = line[0][2].split(',')

    part[i]={'pos':[int(j) for j in p],
            'vel':[int(j) for j in v],
            'acc':[int(j) for j in a],}
for i in range(1000):
    for k in part:
        part[k]['vel'][0]+=part[k]['acc'][0]
        part[k]['vel'][1]+=part[k]['acc'][1]
        part[k]['vel'][2]+=part[k]['acc'][2]
        part[k]['pos'][0]+=part[k]['vel'][0]
        part[k]['pos'][1]+=part[k]['vel'][1]
        part[k]['pos'][2]+=part[k]['vel'][2]
    
    remove =set()
    for k in part:
        for j in part:
            if k!= j and part[k]['pos']==part[j]['pos']:
                remove.add(k)
                remove.add(j)
    print('to remove', len(remove),len(part))
    for i in remove:
        part.pop(i)

def manhattan(inp):
    return abs(inp[0])+abs(inp[1])+abs(inp[2])
dis = [manhattan(part[k]['pos']) for k in part]



l


# %%
