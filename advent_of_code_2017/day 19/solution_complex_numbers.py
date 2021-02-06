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
try:
	os.chdir(os.path.join(os.getcwd(), 'day 19'))
	print(os.getcwd())
except:
	pass

# %%
lines = open('input.txt','r').read().splitlines()
start = lines[0].find('|')+0j
direction = 1j

def getpos(pos):
    return lines[int(pos.imag)][int(pos.real)]
res = []
count = 0
while True:
    count +=1
    if getpos(start).isupper(): 
        res.append(getpos(start))
        if getpos(start) == 'P':
            print(count)
            break
    if getpos(start)=='+':
        if getpos(start+direction*1j) != ' ':
            direction *=1j
        else: direction *=-1j
    start = start+direction
''.join(res)

# %%
