#%%
# always check the input carefully after opening and splitting
# split r and c indices for simplicity (instead of combining them into a tuple)
# when using re, be sure to thing if greedy or nongreedy parsing is necessary
# don't use re when split() suffices, whitespaces can be casted to int
# make sure to experiment with one item from a list instead of and immediate for loop
# !when there is a clear test case available, test it!
# scan over the input a bit more carefully, it may be different than the test examples
# when plotting, use plt.imshow (not plt.show)
# i should look into itertools more
# when refractoring a test case into the real code, check the indices are not hardcoded!
# use better descriptive names. also unpack if it makes code more readable for example in list of tuples
# with regex you can numbers pretty easily in a line. and -? to add possible negatives
# !determine whether bruteforcing is possible can save a lot of time of wasted coding
# %%
num_elves = 3017957
# num_elves = 5

from collections import OrderedDict

circle = OrderedDict()
for i in range(1,num_elves+1):
    circle[i] = 1
while len(circle)>1:
    elves = list(circle.keys())
    # print(circle)
    for e1,e2 in zip(elves[::2],elves[1::2]):
        # print(e1,e2)
        circle[e1] = circle[e1]+circle[e2]
        circle.pop(e2)
        # print(circle)
    if len(elves) % 2 == 1:
        circle[elves[-1]] = circle[elves[-1]]+circle[elves[0]]
        circle.pop(elves[0])
        # print(circle)
circle

# %%
num_elves = 3017957
# num_elves = 5

from collections import OrderedDict

circle = OrderedDict()
for i in range(1,num_elves+1):
    circle[i] = 1
while len(circle)>1:
    elves = list(circle.keys())
    num_elves = len(circle)
    for e1 in elves:
        # print('elf checking e1')
        if circle.get(e1):
            new_elf_list = list(circle.keys())
            elf1_ind = new_elf_list.index(e1)
            elf2_ind = (elf1_ind+num_elves//2)%num_elves)
            circle[e1] = circle[e1]+circle[new_elf_list[elf2_ind]]
            circle.pop(new_elf_list[elf2_ind])
            num_elves -= 1
circle


# %%
num_elves = 3017957
# num_elves = 5


circle = [(i,1) for i in (range(1,num_elves+1))]

while len(circle)>1:
    num_elves_left = len(circle)
    print(num_elves_left)
    for e1 in circle[:]:
        if e1 in circle:
            # print(e1,circle)
            elf1_ind = circle.index(e1)
            elf2_ind = (elf1_ind+num_elves_left//2)%num_elves_left
            e2 = circle[elf2_ind]
            circle[elf1_ind] = (e1[0], e1[1]+e2[1])
            circle.pop(elf2_ind)
            num_elves_left-=1
circle

# %%
num_elves = 3017957
# num_elves = 5

from collections import deque

circle = deque([(i,1) for i in (range(1,num_elves+1))])
num_elves_left = len(circle)
while num_elves_left>1:
    if num_elves_left%1000==0: print(num_elves_left)
    # print('num left',num_elves_left,circle)
    rotate1 = (num_elves_left//2)%num_elves_left
    elf1 = circle.popleft()
    
    circle.rotate(-rotate1+1)
    elf2 = circle.popleft()
    # print(circle,'rotated',rotate1,elf1,elf2)

    # print('new',(elf1[0],elf1[1]+elf2[1]))
    circle.rotate(rotate1-1)
    circle.appendleft((elf1[0],elf1[1]+elf2[1]))
    # print('newcircle',circle,'\n')
    circle.rotate(-1)
    num_elves_left-=1
circle

# %%
num_elves = 3017957

circle = [(i,1) for i in (range(1,num_elves+1))]

while len(circle)>1:
    num_elves_left = len(circle)
    cutoff = (num_elves_left//2)%num_elves_left
    print(num_elves_left)
    addition = 1 if num_elves_left%2==1 else 2
    to_remove = [elf for i,elf in enumerate(circle) if i >= cutoff and (i-cutoff)%3 != addition]
    for i,elf in enumerate(to_remove):
        circle[i]= (circle[i][0],circle[i][1]+elf[1])
    circle = [elf for i,elf in enumerate(circle) if i < cutoff or (i-cutoff)%3 == addition]
    circle = circle[len(to_remove):]+circle[0:len(to_remove)]
circle
# %%