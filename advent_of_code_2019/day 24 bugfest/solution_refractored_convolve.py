# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% De werkmap van de werkruimte root naar de ipynb-bestandslocatie veranderen. Schakel deze toevoeging uit met de instelling DataScience.changeDirOnImportExport
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'day 24'))
	print(os.getcwd())
except:
	pass
from IPython import get_ipython

from scipy import signal
import numpy as np

f=open('input.txt')
grid = np.array([list(l.strip()) for l in f])

kernel = np.zeros((3,3))
kernel[[0,1,1,2],[1,0,2,1]]=1

res = set(''.join(grid.flatten()))

for i in range(13333334):
    bugs = signal.convolve2d(grid=='#', kernel, boundary='fill', mode='same')
    grid = np.select([(grid=='#') & (bugs!=1), (grid=='.') & ((bugs==1) | (bugs==2))],['.','#'],default=grid)
    checksum = ''.join(grid.flatten())
    if checksum in res:
        print('double')
        break
    res.add(checksum)


def biodiversity(grid):
    out = 0
    for i,x in enumerate(grid.flatten()):
        if x=='#': out+=2**i 
    return out

biodiversity(grid)
# %%
#part 2
# copied from https://nbviewer.jupyter.org/github/mjpieters/adventofcode/blob/master/2019/Day%2024.ipynb
f=open('input.txt')
grid = np.array([list(l.strip()) for l in f])
grid[grid == '#']= 1
grid[grid == '.']= 0
grid = grid.astype('int32', copy=False)

grid = np.pad(grid[None], [(200,), (0,), (0,)],mode='constant')

kernel = np.array([
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 1, 0], [1, 0, 1], [0, 1, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
])
for i in range(200):
    bugs = signal.convolve(grid, kernel, mode='same')
    bugs[:,2,2]=0
    # layer below, bugs[:-1, ...] are updated from kernel[1:, ...].sum()s
    bugs[:-1, 1, 2] += grid[1:,  0,  :].sum(axis=1)  # cell above hole += top row next level
    bugs[:-1, 3, 2] += grid[1:, -1,  :].sum(axis=1)  # cell below hole += bottom row next level
    bugs[:-1, 2, 1] += grid[1:,  :,  0].sum(axis=1)  # cell left of hole += left column next level
    bugs[:-1, 2, 3] += grid[1:,  :, -1].sum(axis=1)  # cell right of hole += right column next level
    # layer above, bugs[1-:, ...] slices are updated from kernel[:-1, ...] indices (true -> 1)
    bugs[1:,  0,  :] += grid[:-1, 1, 2, None]  # top row += cell above hole next level
    bugs[1:, -1,  :] += grid[:-1, 3, 2, None]  # bottom row += cell below hole next level
    bugs[1:,  :,  0] += grid[:-1, 2, 1, None]  # left column += cell left of hole next level
    bugs[1:,  :, -1] += grid[:-1, 2, 3, None]  # right column += cell right of hole next level

    grid = np.select([(grid==1) & (bugs!=1), (grid==0) & ((bugs==1) | (bugs==2))],[0,1],default=grid)

print(np.sum(grid==1))





# %%


# %%
