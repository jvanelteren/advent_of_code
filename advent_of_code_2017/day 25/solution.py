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
# i should learn to parse better?

# %%
import os
from dataclasses import dataclass
from collections import deque

try:
	os.chdir(os.path.join(os.getcwd(), 'day 25'))
	print(os.getcwd())
except:
	pass

@dataclass
class state:
    write0:int
    cursor0:int
    nextstate0:str
    write1:int
    cursor1:int
    nextstate1:str

f = open('input.txt','r')
lines = [line.rstrip() for line in f]
states = {}
for i in range(0,len(lines),10):
    write0= int(lines[i+2][-2])
    if 'right' in lines[i+3]: 
        cursor0 = 1
    else:
        cursor0 = -1
    nextstate0 = lines[i+4][-2]
    write1= int(lines[i+6][-2])
    if 'right' in lines[i+7]: 
        cursor1 = 1
    else:
        cursor1 = -1
    nextstate1 = lines[i+8][-2]
    states[lines[i][-2]]= state(write0,cursor0,nextstate0,write1,cursor1,nextstate1)

pos = 0
tape = deque([0])
checksum = 6
checksum = 12481997 
state = 'A'

for i in range(checksum):
    value = tape[pos]
    # print(state,pos,value,tape)
    if value == 0:
        tape[pos]= states[state].write0
        pos+=states[state].cursor0
        state = states[state].nextstate0
    if value == 1:
        tape[pos]= states[state].write1
        pos+=states[state].cursor1
        state = states[state].nextstate1
    if pos<0:
        tape.appendleft(0)
        pos = 0
    if pos == len(tape):
        tape.append(0)
print(sum(tape))