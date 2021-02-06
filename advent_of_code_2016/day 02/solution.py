#%%
# always check the input carefully after opening and splitting

# %%
import numpy as np
f = open('input.txt','r')
code = [line.rstrip() for line in f]
print(f'len lines {len(code)} first item {code[0]}')

# %%
def type(start,keypress):
    # use first grid for part 1, second grid for part 2
    grid = np.arange(1,10).reshape(3,3)
    grid = np.array([list('XX1XX'),list('X234X'),list('56789'),list('XABCX'),list('XXDXX')]).reshape(5,5)
    l = grid.shape[0]
    for k in keypress:
        if k == 'D' and start[0]<grid.shape[0]-1 and grid[(start[0]+1,start[1])]!='X': 
            start[0]+=1
        if k == 'U' and start[0]>0 and grid[(start[0]-1,start[1])]!='X': 
            start[0]-=1
        if k == 'L' and start[1]>0 and grid[(start[0],start[1]-1)]!='X': 
            start[1]-=1
        if k == 'R' and start[1]<grid.shape[0]-1 and grid[(start[0],start[1]+1)]!='X': 
            start[1]+=1
    print(grid[tuple(start)])
    return start
    
start = [1,1]
for keypress in code:
    start = type(start,keypress)


# %%
