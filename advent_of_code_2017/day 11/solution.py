#%%
# read full assignment
# think algo before implementing
# dont use a dict when you need a list
# assignment is still = and not ==
# dont use itertools when you can use np.roll
# check mathemathical functions if the parentheses are ok
# %%
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'day 11'))
	print(os.getcwd())
except:
	pass

f = open('input.txt','r').read().strip().split(',')
pos = [0,0]
move = {
    'n':[0,2],
    'ne':[1,1],
    'se':[1,-1],
    's':[0,-2],
    'sw':[-1,-1],
    'nw':[-1,1],
}
def dis(pos):
    return (abs(pos[1])-abs(pos[0]))/2+abs(pos[0])
maximum = 0
for m in f:
    pos = [pos[0]+move[m][0],pos[1]+move[m][1]]
    print(pos,dis(pos))
    if dis(pos)> maximum: maximum = dis(pos)
maximum
# %%
