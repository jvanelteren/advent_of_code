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
# %%
import os
import re
import numpy as np
import string

try:
	os.chdir(os.path.join(os.getcwd(), 'day 16'))
	print(os.getcwd())
except:
	pass

f = open('input.txt','r').read().rstrip().split(',')
ins = [re.findall('(.)(.+)/(.*)',line) for line in f]
for ind,i in enumerate(ins):
    if not i:
        ins[ind]=re.findall('(.)(.*)',f[ind])
# %%
def spin(array, inp):
    return np.roll(array,inp)

def exchange(array,a,b):
    array[a], array[b]= array[b],array[a]
    return array

def partner(array,a,b):
    a = np.where(array==a)
    b = np.where(array==b)
    return exchange(array,a,b)

# %%
d = string.ascii_lowercase[:16]
d = np.array(list(d))
res = [''.join(d)]
for dance in range(10000):
    for i in ins:
        i = i[0]
        if i[0]=='x':
            d = exchange(d,int(i[1]),int(i[2]))
        if i[0]=='s':
            d = spin(d,int(i[1]))
        if i[0]=='p':
            d = partner(d,i[1],i[2])
    if ''.join(d) in res:
        print('duplicate detected')
        break
    res.append(''.join(d))
#part 1
print(res[1])
#part 2    
print(res[1000000000 % len(res)])

# %%