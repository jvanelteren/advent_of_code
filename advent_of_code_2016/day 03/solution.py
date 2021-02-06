#%%
# always check the input carefully after opening and splitting
# split r and c indices for simplicity (instead of combining them into a tuple)
# when using re, be sure to thing if greedy or nongreedy parsing is necessary
# don't use re when split() suffices, whitespaces can be casted to int
# %%

f = open('input.txt','r')

lines = [line.rstrip() for line in f]
print(f'len lines {len(lines)} first item {lines[0]}')

# %%
triangles = [list(map(int,l.split())) for l in lines]

# %%
def istriangle(t):
    if t[0]+t[1]>t[2] and t[1]+t[2]>t[0] and t[0]+t[2]>t[1]:
        return True
    else: return False
len([t for t in triangles if istriangle(t)])

# %%
res = []
for l in range(0,len(triangles),3):
    for i in range(3):
        if istriangle([triangles[l][i],triangles[l+1][i],triangles[l+2][i]]): res.append(1)
sum(res)
