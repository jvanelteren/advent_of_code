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

# approach 1 with a queue, the most elegant
num_elves = 3017957
from collections import deque

circle = deque((range(1,num_elves+1)))
num_elves_left = len(circle)
rotate = (num_elves_left//2)%num_elves_left
circle.rotate(-rotate) # rotate to initial position
elf1 = circle.popleft()
num_elves_left-=1
while num_elves_left>1:
    if num_elves_left%2==0:
        circle.rotate(-1) # skip 1 if even, pop next if odd
    circle.popleft()
    num_elves_left-=1
circle

# %%
# approach 2 with a list

num_elves = 3017957
circle = [i for i in (range(1,num_elves+1))]
while len(circle)>1:
    num_elves_left = len(circle)
    cutoff = (num_elves_left//2)%num_elves_left
    addition = 1 if num_elves_left%2==1 else 2
    circle = [elf for i,elf in enumerate(circle) if i < cutoff or (i-cutoff)%3 == addition]
    circle = circle[num_elves_left-len(circle):]+circle[0:num_elves_left-len(circle)]
circle
# %%