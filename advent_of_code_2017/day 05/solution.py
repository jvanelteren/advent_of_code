#%%
# read full assignment
# think algo before implementing
f = open('input.txt','r').read().split()
ins = [int(i) for i in f]
#%%
start = 0
for i in range(1,100000000):
    if ins[start]>= 3:
        ins[start]-=1
        start += ins[start]+1
    else:
        ins[start]+=1
        start += ins[start]-1
    if start>= len(ins):
        print(i)
        break
# %%
