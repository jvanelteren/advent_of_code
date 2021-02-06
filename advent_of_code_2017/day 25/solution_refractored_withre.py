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
# i should learn to parse better? --> use re findall with multiline instructions
# when parsing difficult stuff, it sometimes cannot be done with list comprehension. use for loop with append
# %%
import os
from dataclasses import dataclass
from collections import deque,defaultdict
import re

try:
	os.chdir(os.path.join(os.getcwd(), 'day 25'))
	print(os.getcwd())
except:
	pass

@dataclass
class state:
    write:int
    cursor:int
    nextstate:str

f = open('input.txt','r').read()
parsed = re.findall('In state (.+):\n  If the current value is (.+):\n    - Write the value (.+).\n    - Move one slot to the (.+).\n    - Continue with state (.+).\n  If the current value is (.+):\n    - Write the value (.+).\n    - Move one slot to the (.+).\n    - Continue with state (.+).', f)
states = {}

for s in parsed:
    states[s[0],int(s[1])] = state(int(s[2]),s[3],s[4])
    states[s[0],int(s[5])] = state(int(s[6]),s[7],s[8])

pos = 0
tape = defaultdict(lambda: 0)
checksum = 12481997
state = 'A'

for i in range(checksum):
    value = tape[pos]
    tape[pos] = states[(state,value)].write
    if states[(state,value)].cursor == 'right': pos+=1
    else: pos-=1
    state = states[(state,value)].nextstate
sum(tape.values())