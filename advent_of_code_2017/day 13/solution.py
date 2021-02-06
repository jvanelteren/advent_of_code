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
import re
import numpy as np

try:
	os.chdir(os.path.join(os.getcwd(), 'day 13'))
	print(os.getcwd())
except:
	pass

f = open('input.txt','r')
layers = {int(line.rstrip().split(': ')[0]):int(line.rstrip().split(': ')[1]) for line in f}
layers

for x in range(10000):
    severity = 0

    for pos in range(100):
        if layers.get(pos,None):
            # print(pos,layers[pos])
            divisor = (layers[pos]-1)*2
            if (pos+x+x)% divisor==0:
                # print('hit',pos)
                severity+=pos*layers[pos]+1
                break
    if severity== 0: 
        print('succes',x)
        break

severity
# %%
