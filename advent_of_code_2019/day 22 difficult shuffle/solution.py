# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% De werkmap van de werkruimte root naar de ipynb-bestandslocatie veranderen. Schakel deze toevoeging uit met de instelling DataScience.changeDirOnImportExport
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'day 22'))
	print(os.getcwd())
except:
	pass
from IPython import get_ipython
import numpy as np
import re
import math

#tried to develop this one in the VSCode interactive environment
#THIS CODE IS A HORRIBLE MESS

# %%
deck = np.arange(10)
def cut(arr,i):
    return np.roll(arr,-i)

def deal_inc(arr,inc):
    l = len(arr)
    ind = np.zeros(l).astype(int)
    start = 0
    number =0
    for i in range(inc):
        ind[start::inc]=range(number,number+math.ceil((l-start)/inc))
        number += math.ceil((l-start)/inc)
        left = (l-start)%inc
        start = (inc-left)%inc
    
    return arr[ind]
print(deal_inc(deck, 7))

def deal_stack(arr):
    return  arr[::-1]
print(deal_stack(deck))
# %%
def shuffle(deck):
    for i in ins:
        i= i[0]
        if i[0] == 'deal with increment ':
            deck = deal_inc(deck,int(i[1]))
        elif i[0] == 'cut ':
            deck = cut(deck,int(i[1]))

        elif i[0] == 'deal into new ':
            deck = deal_stack(deck)

    return deck

f = open('input.txt','r')
lines = [lines.rstrip() for lines in f]
ins = [re.findall('(.+ )(-?\d+)?',l) for l in lines]
deck_len = 100
# deck_len = 119315717514047
deck = np.arange(deck_len)

for i in range(10):
    print(deck[2019:2021])
    deck = shuffle(deck)
    




# %%
primes = [11,13,17,	19,	23,	29,31]
for dl in range(1000,1010):
    deck = np.arange(dl)
    res = []
    for i in range(100):
        res.append(deck[c])
        deck = shuffle(deck)
        if all(deck == np.arange(dl)): 
            print('research deck len',dl,'same',i)
            break
# %%
np.argwhere(deck==2019)

# %%
from math import sqrt
from functools import reduce
def factors(n):
        step = 2 if n%2 else 1
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))


# %%
# reverse engineer the functions


import numpy as np
deck = np.arange(10)
def rev_cut(v,arg,len):
    return (v+arg)%len

for i in range(10):
    print(rev_cut(i,3,10))

def rev_deal_inc(v,arg,len):
    arraymod = 0
    count = 0
    if v%arg==0: # if the index is a whole of the shift
        return v//arg # then it was simply placed in the first round of placing
    else:
        while True:
            # print(rounds)
            count += math.ceil((len-arraymod)/arg)
            arraymod = arg-(len-arraymod)%arg
            offsetmod = (v-arraymod) % arg
            if offsetmod ==0:
                return count + v//arg

# print(rev_deal_inc(2020,54088161892304,119315717514047))

def rev_stack(v,len):
    return(len-1-v)

# %%
def shuffle(v,len,ins):
    # res = []
    for i in ins[::-1]:
        i= i[0]
        if i[0] == 'deal with increment ':
            v = rev_deal_inc(v,int(i[1]),len)
        elif i[0] == 'cut ':
            v = rev_cut(v,int(i[1]),len)
        elif i[0] == 'deal into new ':
            v = rev_stack(v,len)
        # print(v)
    return v

f = open('input.txt','r')
lines = [lines.rstrip() for lines in f]
ins = [re.findall('(.+ )(-?\d+)?',l) for l in lines]
deck_len = 119315717514047
# deck_len = 119315717514047
print(shuffle(2020,deck_len,ins))

res = []
start = 2020
for i in range(10):
    res.append(shuffle(start,deck_len,ins))
    start = res[-1]
print(res)
for i in zip(res,res[1:]): print(i[1]-i[0])
# print (res)


# %%
for i in zip(res[:100],res[1:101]): print(i[1]-i[0])
# %%
from matplotlib import pyplot
pyplot.plot(res)
# %%
def forward_cut(v,arg,len):
    return(v-arg)%len


def forward_deal_inc(v,inc,len):
    l = len
    start = 0
    number =0

    while True:
        adding = math.ceil((l-start)/inc)
        if number + adding>v:
            return start + inc*(v-number)
        else:
            number+=adding
            left = (l-start)%inc
            start = (inc-left)%inc
def forward_stack(v,len):
    return(len-1-v)

def shuffle(v,len,ins):
    # res = []
    for i in ins:
        i= i[0]
        if i[0] == 'deal with increment ':
            v = forward_deal_inc(v,int(i[1]),len)
        elif i[0] == 'cut ':
            v = forward_cut(v,int(i[1]),len)
        elif i[0] == 'deal into new ':
            v = forward_stack(v,len)
        # print(v)
    return v

import re
f = open('input.txt','r')
lines = [lines.rstrip() for lines in f]
ins = [re.findall('(.+ )(-?\d+)?',l) for l in lines]
deck_len = 119315717514047


print(shuffle(2020,deck_len,ins))
# print(shuffle(65227555623763,deck_len,ins))
res = []
start = 1193157175140
for i in range(10):
    res.append(shuffle(start,deck_len,ins))
    start = res[-1]
for i in zip(res,res[1:]): 
    if i[1]-i[0]<0:
        print(i[1]-i[0])
    else: print(i[1]-i[0]+l)
print (res)
# 13035406070497
# 90946404012537
# 79090535172416 too high
# 55836183599565 too low
# 119315717514047 deck len
# 109924345491869
# gold 54088161892304
# %%

gold = 54088161892304
l = 119315717514047

# %%
def previous(i,p):
    return (i+(i-p)*gold)*%l

previous(119315717514047,96873435858537)

# %%
base = 90946404012537
gold = 54088161892304
# 99999999999999999 
l = 119315717514047
shuf = 101741582076661
t = [base,gold,l,shuf]
for t1 in t:
    for t2 in t:
        print(t1%t2)
def prev(i):
    return (base+gold*i)%l

prev(12139369866491111222698357067)
