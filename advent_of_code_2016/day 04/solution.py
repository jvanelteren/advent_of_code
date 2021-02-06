#%%
# always check the input carefully after opening and splitting
# split r and c indices for simplicity (instead of combining them into a tuple)
# when using re, be sure to thing if greedy or nongreedy parsing is necessary
# don't use re when split() suffices, whitespaces can be casted to int
# make sure to experiment with one item from a list instead of and immediate for loop
# %%
import re
from collections import Counter
import string

f = open('input.txt','r')
lines = [line.rstrip() for line in f]
print(f'len lines {len(lines)} first item {lines[0]}')
checks =  [re.findall('(.+?)(\d+)\[(.+)\]',l) for l in lines]
checks[0]
# %%
valid = []
results = []
for c in checks:
    c = c[0]
    test = c.replace('-','')
    counts = Counter(test).most_common()
    counts.sort(key=lambda x: [-x[1],x[0]])
    checksum = ''.join([c[0] for c in counts][:5])
    if checksum == c[2]: 
        valid.append(int(c[1]))
        results.append(c)
sum(valid)
# %%
res = []
letters = string.ascii_lowercase

for c in results:
    print(c)
    res.append((''.join([letters[(letters.index(l)+int(c[1]))%26] for l in c[0] if l !='-']),c[1]))
res.sort(key=lambda x:x[1])
for i in res:
    if int(i[1])>700:
        print(i[0],i[1])

# %%
