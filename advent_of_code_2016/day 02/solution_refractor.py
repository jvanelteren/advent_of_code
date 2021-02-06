#%%
# always check the input carefully after opening and splitting
# split r and c indices for simplicity (instead of combining them into a tuple)
#
# %%
f = open('input.txt','r')
code = [line.rstrip() for line in f]
print(f'len lines {len(code)} first item {code[0]}')

# %%
def type(r,c,keypress):
    # use first grid for part 1, second grid for part 2
    # grid = np.arange(1,10).reshape(3,3)
    grid = np.array([list('XX1XX'),list('X234X'),list('56789'),list('XABCX'),list('XXDXX')]).reshape(5,5)
    l = grid.shape[0]
    for k in keypress:
        if k == 'D' and r<l-1 and grid[r+1][c]!='X': 
            r+=1
        if k == 'U' and r>0 and grid[r-1][c]!='X': 
            r-=1
        if k == 'L' and c>0 and grid[r][c-1]!='X': 
            c-=1
        if k == 'R' and c<l-1 and grid[r][c+1]!='X': 
            c+=1
    print(grid[r][c])
    return r,c

r,c = 1,1
for keypress in code:
    r,c = type(r,c,keypress)


# %%
