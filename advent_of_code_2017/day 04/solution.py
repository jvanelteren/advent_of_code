#%%
with open('input.txt','r') as f:
    passphrases = [line.split() for line in f]
passphrases = ([p for p in passphrases if len(p)==len(set(p))])
print(len(passphrases))    
#%%
ans = 0
for p in passphrases:
    if len({''.join(sorted(w)) for w in p}) == len({w for w in p}):
        ans+=1
print(ans)
# %