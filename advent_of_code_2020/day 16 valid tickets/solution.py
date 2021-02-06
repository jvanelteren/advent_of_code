# reminder: sets can be tricky dont use when duplicate values are important
#%%
import aoc
from collections import defaultdict

f=open('nearby.txt')
lines = [aoc.to_int(line.rstrip('\n').split(',')) for line in f]
yourticker = [89,139,79,151,97,67,71,53,59,149,127,131,103,109,137,73,101,83,61,107]
# %%

f=open('input.txt')
conditions = [line.rstrip('\n').split(': ') for line in f]
cond = dict()
for c, val in conditions:
    vals = aoc.to_int(val.split(" or "))
    vals = tuple(aoc.to_int(v.split('-')) for v in vals)
    cond[c] = vals
# %%
invalids = []
for line in lines[:]:
    for l in line:
        for c, val in cond.items():
            if (l in range(val[0][0],val[0][1]+1)) or (l in range(val[1][0],val[1][1]+1)):
                break
        else:
            invalids.append(l)
            lines.remove(line)
sum(invalids)


# %%
# part 2
options  = defaultdict(list)

for c, val in cond.items():
    for i in range(len(cond)):
        valid = True
        for line in lines:
            if (line[i] in range(val[0][0],val[0][1]+1)) or (line[i] in range(val[1][0],val[1][1]+1)):
                pass
            else:
                valid = False
        if valid:
            options[c].append(i)

# %%
to_assign = set(list(range(len(cond))))
removed = []
final = dict()

while to_assign:
    for k,v in options.items():
        if len(v)==1:
            to_assign.remove(v[0])
            removed.append(v[0])
            final[k]=v[0]
    for k,v in final.items():
        if k in options:
            del options[k]
    for r in removed:
        for k in options.keys():
            if r in options[k]:
                options[k].remove(r)


# %%
ans = 1
for k,v in final.items():
    if 'departure' in k:
        ans *= yourticker[v]
ans

# %%
