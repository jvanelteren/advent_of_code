# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
from math import gcd, ceil
import re
import networkx as nx
from dataclasses import dataclass
import itertools
import aoc
from matplotlib import pyplot as plt
import string
# plt.imshow(pic)


# %%

# %%
type(code)
#%%
from collections import Counter, defaultdict, namedtuple, deque



def step(code, minim, maxim, current_index):
    # print(code)

    current_cup = code[current_index]
    code.rotate(-current_index-1)
    # print('rotated', code)
    pickup = [code.popleft()]+[code.popleft()]+[code.popleft()]
    # print('pickup',pickup)

    
    # print('index',current_index, 'which is', current_cup)
    current_cup = current_cup - 1
    if current_cup < MINIM:
        # print('wrap around')
        current_cup = MAXIM # NEED TO BE MADE MAX
    while current_cup in pickup:
        current_cup -= 1
        if current_cup < MINIM:
            # print('wrap around')
            current_cup = MAXIM # NEED TO BE MADE MAX
    
    # print('destination',current_cup)
    insert = code.index(current_cup)+1
    print(insert)
    # insert = 0 THIS IS THE PROBLEM


    # print('destination', insert)
    # print(code, insert)
    to_rot = len(code) -insert
    code.rotate(to_rot)
    

    code.append(pickup[0])
    code.append(pickup[1])
    code.append(pickup[2])
    code.rotate(-to_rot)
    # print(code)

    code.rotate(current_index+1)
    # print('\n')
    current_index = (current_index + 1) % len(code)
    # print(insert, code.index(1))
    return code, current_index


for l in [1000000]:
    # code = "916438275"
    # code = "389125467"
    # code = "389125467"
    code = "123456789"
    code = deque(int(c) for c in code)
    # code += list(range(10, 1000001))
    code += list(range(10, l+1))
    MINIM = min(code)
    MAXIM = max(code)
    current_index = 0


    for s in range(1000):
        # if s % len(code) == 0: print(code)
        # print(code)
        code, current_index = step(code, MINIM, MAXIM, current_index)
        # i = code.index(1)
        # print(list(code)[i-10:i+30])
        i = code.index(1)
        print(l, list(code)[i:i+10], s)
    # print(l, code)
    i = code.index(1)
    print(l, list(code)[i:i+3])
# %%
code = "916438275"
# code = "389125467"
code = "389125467"
code = list(int(c) for c in code)
# code += list(range(10, 10000001))
MINIM = min(code)
MAXIM = max(code)

num_to_loc = {}
loc_to_num = {}

for index, i in enumerate(code):
    num_to_loc[i] = index
    loc_to_num[index] = i
SIZE = len(num_to_loc)
round = 1
current_index = 0
for i in range(5):
    print('round', round)
    print([loc_to_num[i] for i in range(9)])
    current_cup = loc_to_num[current_index]
    
    pickup = [loc_to_num[current_index+1],loc_to_num[current_index+2],loc_to_num[current_index+3]]
    print(pickup)
    # print('pickup',pickup)
    current_cup = current_cup - 1
    if current_cup < MINIM:
        # print('wrap around')
        current_cup = MAXIM # NEED TO BE MADE MAX
    while current_cup in pickup:
        current_cup -= 1
        if current_cup < MINIM:
            # print('wrap around')
            current_cup = MAXIM # NEED TO BE MADE MAX
    print(current_cup)
    insert = num_to_loc[current_cup]+1
    if insert > current_index+1: insert-=3
    print(current_index+1, insert)

    delta = insert - (current_index+1)
    print('delta', delta)

    if delta >=0:
        num_to_loc[pickup[0]] = (num_to_loc[pickup[0]] + delta) % SIZE
        # print('done', pickup[0],num_to_loc[pickup[0]])
        num_to_loc[pickup[1]] = (num_to_loc[pickup[1]] + delta) % SIZE
        num_to_loc[pickup[2]] = (num_to_loc[pickup[2]] + delta) % SIZE

        for i in range(delta):
            nextnum = loc_to_num[current_index+4+i]
            loc_to_num[current_index+1+i] = nextnum
            num_to_loc[nextnum] = (num_to_loc[nextnum] -3) % SIZE
        
        for j in range(1,4):
            loc_to_num[current_index+j+delta] = pickup[j-1]
    else:
        num_to_loc[pickup[0]] = (num_to_loc[pickup[0]] + delta) % SIZE
        # print('done', pickup[0],num_to_loc[pickup[0]])
        num_to_loc[pickup[1]] = (num_to_loc[pickup[1]] + delta) % SIZE
        num_to_loc[pickup[2]] = (num_to_loc[pickup[2]] + delta) % SIZE

        for i in range(delta):
            nextnum = loc_to_num[current_index+4+i]
            loc_to_num[current_index+1+i] = nextnum
            num_to_loc[nextnum] = (num_to_loc[nextnum] -3) % SIZE
        
        for j in range(1,4):
            loc_to_num[current_index+j+delta] = pickup[j-1]
        



    current_index = (current_index+1)%len(num_to_loc)
    round+=1
    
    



