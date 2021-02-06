#%%
# always check the input carefully after opening and splitting
# split r and c indices for simplicity (instead of combining them into a tuple)
# when using re, be sure to thing if greedy or nongreedy parsing is necessary
# don't use re when split() suffices, whitespaces can be casted to int
# make sure to experiment with one item from a list instead of and immediate for loop
# when there is a clear test case available, test it!
# scan over the input a bit more carefully, it may be different than the test examples
# %%

import re

f = open('input.txt','r')
lines = [line.rstrip() for line in f]
print(f'len lines {len(lines)} first item {lines[0]}')

falseip = [re.findall('\[(.*?)\]',l) for l in lines]
trueip = [re.sub('\[(.*?)\]',',',l).split(',') for l in lines]

# %%
def isabba(a,b,c,d):
    if a == d and b == c and a != b: return True
    else: return False

def support_tls(subs):
    # the below was a bit refractored. It looks difficult though
    return any(any(isabba(a,b,c,d) for a,b,c,d in zip(s,s[1:],s[2:],s[3:])) for s in subs)

def isbab(a,b,c,d,e,f):
    if d == f and d != e and a == e and b == d: return True
    else: return False

def isaba(a,b,c,hyper):
    if a == c and a != b and b != c:
        for s in hyper:
            if True in [isbab(a,b,c,d,e,f) for d,e,f in zip(s,s[1:],s[2:])]:
                return True
    else: return False

def support_ssl(subs,hyper):
    for s in subs:
        if True in [isaba(a,b,c,hyper) for a,b,c in zip(s,s[1:],s[2:])]:
            return True
    else: return False

# %%
# part 1
sum([support_tls(trueip[i]) for i in range(len(trueip)) if not support_tls(falseip[i])])

# %%
# part 2
sum([support_ssl(trueip[i],falseip[i]) for i in range(len(trueip))])
# %%

# reddit, nice solution making it into two strings for the supernet and hypernet
import re
def abba(x):
    return any(a == d and b == c and a != b for a, b, c, d in zip(x, x[1:], x[2:], x[3:]))
lines = [re.split(r'\[([^\]]+)\]', line) for line in open('test0.txt')]
parts = [(' '.join(p[::2]), ' '.join(p[1::2])) for p in lines]
print('Answer #1:', sum(abba(sn) and not(abba(hn)) for sn, hn in parts))
print('Answer #2:', sum(any(a == c and a != b and b+a+b in hn for a, b, c in zip(sn, sn[1:], sn[2:])) for sn, hn in parts))
lines
