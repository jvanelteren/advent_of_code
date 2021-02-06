#%%
# read full assignment
# think algo before implementing
# %%
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'day 08'))
	print(os.getcwd())
except:
	pass

import re
from collections import namedtuple, OrderedDict
f = open('input.txt','r')
lines = [line.split() for line in f]
ins = namedtuple('ins',['reg','opcode','value'])
cond = namedtuple('cond',['reg','comparison','value'])
instructions = []
for line in lines:
    instructions.append((ins(line[0],line[1],line[2]),cond(line[4],line[5],line[6])))

# %%
registers = {k.reg:0 for k,v in instructions}
maximum = 0
for k,v in instructions:
    if eval(str(registers[v.reg])+str(v.comparison)+str(v.value)):
        if k.opcode =='dec':
            registers[k.reg]-=int(k.value)
            if registers[k.reg] > maximum: maximum = registers[k.reg]
        if k.opcode =='inc':
            registers[k.reg]+=int(k.value)
            if registers[k.reg] > maximum: maximum = registers[k.reg]

#part 1
max(registers.values())
#part 2
maximum

# %%
