# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
from collections import Counter, defaultdict, namedtuple, deque
from math import gcd, ceil
import re
import networkx as nx
from dataclasses import dataclass
import itertools
import aoc_utils
from matplotlib import pyplot as plt
import string
# plt.imshow(pic)


# %%
f = open('test.txt').read().split('\n\n')
rules = f[0].split('\n')
messages = f[1].split('\n')


# %%
rulebook = {}
for r in rules:
    num, ins = r.split(': ')
    ins = ins.replace('"','')
    ins_piped = [i.split() for i in ins.split('|')]
    if len(ins_piped[0])==1 and ins_piped[0][0] in 'ab':
        ins_piped = ins_piped[0][0]
    rulebook[num]=ins_piped


# %%
rulebook


# %%
from collections import namedtuple

def test(message, rules, r):
    print('called', message, r)
    if rules[r]=='a' or rules[r]=='b':
        print('endpoint reached',message and message[0] == rules[r])
        return {1,} if (message and message[0] == rules[r]) else set()
    else:
        overall_matches = set()
        for opt in rules[r]:
            opt_match = {0,}
            for rule in opt: # 4,1,5
                new_match = set() 
                for n in opt_match: 
                    new_match |= {n+m for m in test(message[n:],rules,rule)}
                opt_match = new_match
            overall_matches |= opt_match
        print('returning', overall_matches) 
        return overall_matches

print("Part 1:", sum(len(m) in test(m,rulebook,'0') for m in messages))


# %%
