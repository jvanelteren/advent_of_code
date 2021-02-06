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
# dict of dataclass works better than dict of dicts
# convolutions are not so easy to implement


# %%
import os
import numpy as np
import re
from collections import Counter

try:
	os.chdir(os.path.join(os.getcwd(), 'day 21'))
	print(os.getcwd())
except:
	pass
from dataclasses import dataclass
@dataclass
class Pos:
    pos:list
    vel:list
    acc:list

# %%
f = open('input.txt','r')
lines = [[i for i in line.rstrip().split(' => ')]for line in f]
inp,out = [],[]
for line in lines:
    inp.append(np.array([list(l) for l in line[0].split('/')]))
    out.append(np.array([list(l) for l in line[1].split('/')]))

#%%
def convolve(arr):
    s = arr.shape[0]
    kernel = 2 if s % 2==0 else 3
    conv = []
    for x in range(0,s,kernel):
        for y in range(0,s,kernel):
            conv.append(arr[x:x+kernel,y:y+kernel])
    return conv

def findmatch(arr):
    s = arr.shape[0]
    for c,i in enumerate(inp):
        if i.shape[0]==s:
            for _ in range(4):
                arr = np.rot90(arr)
                if np.array_equal(i,arr):
                    return out[c]
                if np.array_equal(i,np.flip(arr,1)):
                    return out[c]
                if np.array_equal(i,arr):
                    return out[c]
                if np.array_equal(i,np.flip(arr,1)):
                    return out[c]
            
# %%

def concat(conv):
    n_conv = (len(conv))
    rows = int(n_conv**0.5)
    blocks = []
    for i in range(0,n_conv,rows):
        print(n_conv,rows,i)
        blocks.append(np.concatenate((conv[i:i+rows]),axis=1))
    newpattern = np.concatenate(blocks,axis=0)
    print(len(newpattern[newpattern =='#']))
    return newpattern

pattern = np.array([['.','#','.'],['.','.','#'],['#','#','#']])
for i in range(5):
    convolution = convolve(pattern)
    conv = [findmatch(i) for i in convolution]
    pattern = concat(conv)
    print(i,pattern.shape)

# %%
# part 2
def findmatchindex(arr):
    s = arr.shape[0]
    for c,i in enumerate(inp):
        if i.shape[0]==s:
            for _ in range(4):
                arr = np.rot90(arr)
                if np.array_equal(i,arr):
                    return c
                if np.array_equal(i,np.flip(arr,1)):
                    return c
                if np.array_equal(i,arr):
                    return c
                if np.array_equal(i,np.flip(arr,1)):
                    return c

counts = [findmatchindex(i) for i in convolve(pattern)]
counts = Counter(counts)

def returncount(p):
    for i in range(9):
        convolution = convolve(p)
        # print(convolution,len(convolution))
        conv = [findmatch(i) for i in convolution]
        p = concat(conv)
        # print(i,p.shape)
    return len(p[p =='#'])

res = 0
for c in counts:
    res += counts[c]*returncount(inp[c])
res

# %%
