#%%
# read full assignment
# think algo before implementing
# %%
import re
f = open('input.txt','r')
lines = [line.rstrip() for line in f]

tower = {}
for line in lines:
    # print(line)
    if len(re.findall('(.+) -> (.+)',line)) == 0:
        tower[tuple(line.split())]= []
    else:
        res = re.findall('(.+) -> (.+)',line)[0]
        tower[tuple(res[0].split())] =res[1].replace(" ", "").split(',')
children = [i for v in tower.values() for i in v  if isinstance(v,list)]
for k in tower:
    if k[0] not in children:
        print (k)
weights = {k[0]:int(k[1][1:-1]) for k,v in tower.items()}
tower = {k[0]:v for k,v in tower.items()}
# %%

# %%
def weight(child):
    return weights[child]+sum([weight(sub) for sub in tower[child]])
for k,v in tower.items():
    subsets = {weight(child) for child in v}
    if len(subsets)>1:
        print (k, subsets)
        for child in v:
            print(child,weight(child))


# %%
for child in tower['cwwwj']:
    print(child,weight(child))

# %%
weights['cwwwj']

# %%
