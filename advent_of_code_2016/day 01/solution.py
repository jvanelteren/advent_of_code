#%%
# always check the input carefully after opening and splitting

# %%
lines = open('input.txt','r').read().split(', ')

direction = complex(-1,0)
location = complex(0,0)
locs = [location]
for l in lines:
    if l[0]=='L': direction *= 1j
    if l[0]=='R': direction *= -1j
    for dis in range(int(l[1:])):
        location += direction
        if location in locs:
            print('recurring found',abs(location.real)+abs(location.imag))
        locs.append(location)
# part 2
print('final position',abs(location.real)+abs(location.imag))
# %%
lines = open('input.txt','r').read().split(', ')

direction = complex(0,1)
location = complex(0,0)
locs = [location]
for l in lines:
    if l[0]=='L': direction *= 1j
    if l[0]=='R': direction *= -1j
    for dis in range(int(l[1:])):
        location += direction
        if location in locs:
            print('recurring found',abs(location.real)+abs(location.imag))
        locs.append(location)
# part 2
print('final position',abs(location.real)+abs(location.imag))
# %%
