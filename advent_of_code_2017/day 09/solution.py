#%%
# read full assignment
# think algo before implementing
# dont use a dict when you need a list
# assignment is still = and not ==
# %%
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'day 09'))
	print(os.getcwd())
except:
	pass

import re
from collections import namedtuple, OrderedDict
f = open('input.txt','r').read()
# %%
# f = '{{<a!>},{<a!>},{<a!>},{<ab>}}'
level = 0
score = 0
garbage = False
exclamation = False
count = 0
for c in f:
    if not garbage:
        if c == '{':
            level += 1
            score += level
            # print(score)
        if c == '}':
            level -= 1
        if c == '<':
            garbage = True
    else: # garbage
        if exclamation:
            exclamation = False
        else:
            if c == '>':
                garbage = False
            elif c == '!':
                exclamation = True
            else: count +=1

print(score,count) 
  