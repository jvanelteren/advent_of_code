#%%
# read full assignment
# think algo before implementing
# %%
f = open('input.txt','r').read().split()
ins = [int(i) for i in f]
import copy
# ins = [0, 2, 7,  0]
seen = [ins.copy()]
for x in range(1,100000):
    ind = ins.index(max(ins))
    to_rest = ins[ind]
    ins[ind]=0
    start = (ind+1)%len(ins)
    # print(ind,to_rest,start)
    while to_rest>0:
        ins[start]+=1
        start = (start+1)%len(ins)
        to_rest -=1
    if ins in seen:
        print(x)
        break
    else:
        seen.append(ins.copy())

# %%
search = copy.deepcopy(seen[-1])
ins = copy.deepcopy(seen[-1])
for x in range(1,100000):
    ind = ins.index(max(ins))
    to_rest = ins[ind]
    ins[ind]=0
    start = (ind+1)%len(ins)
    # print(ind,to_rest,start)
    while to_rest>0:
        ins[start]+=1
        start = (start+1)%len(ins)
        to_rest -=1
    if ins == search:
        print(x)
        break
# %%
