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
# %%
import os
import re
import numpy as np

try:
	os.chdir(os.path.join(os.getcwd(), 'day 15'))
	print(os.getcwd())
except:
	pass

def gena():
    start = 873
    factor = 16807
    mod = 2147483647
    while True:
        start = (start*factor)%mod
        if start%4 ==0:
            yield start
def genb():
    start = 583
    factor = 48271
    mod = 2147483647
    while True:
        start = (start*factor)%mod
        if start%8 ==0:
            yield start

a = gena()
b = genb()
matches = 0
for i in range(5000000):
    if next(a) & 0xffff ==next(b) & 0xffff: matches+=1
matches


# %%
0xffff&1
# %%
