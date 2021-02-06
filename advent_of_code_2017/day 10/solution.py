#%%
# read full assignment
# think algo before implementing
# dont use a dict when you need a list
# assignment is still = and not ==
# dont use itertools when you can use np.roll
# %%
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'day 10'))
	print(os.getcwd())
except:
	pass

import numpy as np
from functools import reduce
import operator

f = open('input.txt','r').read().strip().split(',')
lengths = [int(l) for l in f]
circular = np.arange(256)
skip = 0
start = 0
for l in lengths:
    circular = np.roll(circular,-start)
    circular[:l]=circular[:l][::-1]
    circular = np.roll(circular,+start)
    start = (start + l + skip)%len(circular)
    skip +=1
circular[0]*circular[1]

# %%
# part 2
f = open('input.txt','r').read().strip()
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
    hashcode +=  hex(densehash(circular[i*16:i*16+16]))[2:]
hashcode


# %%
