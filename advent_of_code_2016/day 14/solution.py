#%%
# always check the input carefully after opening and splitting
# split r and c indices for simplicity (instead of combining them into a tuple)
# when using re, be sure to thing if greedy or nongreedy parsing is necessary
# don't use re when split() suffices, whitespaces can be casted to int
# make sure to experiment with one item from a list instead of and immediate for loop
# !!when there is a clear test case available, test it!
# scan over the input a bit more carefully, it may be different than the test examples
# when plotting, use plt.imshow (not plt.show)
# i should look into itertools more
# when refractoring a test case into the real code, check the indices are not hardcoded!
# use better descriptive names. also unpack if it makes code more readable for example in list of tuples
# with regex you can numbers pretty easily in a line. and -? to add possible negatives
# sometimes its easier to brute force bfs than to figure out an insane algo yourself
# at beginning look at example first and highlighted texts
# utils for bfs make you really fast! boom place 13 on leaderboard
# try to bruteforce if not clear if you have to take a smart shortcut
# when checking if string appears in list of strings, be careful to use ' '.join not ''.join

# %%
import hashlib
import re
salt = 'cuanljph'
threes = []
hashes = []
for i in range(25000):
    initial = hashlib.md5((salt+str(i)).encode('utf-8')).hexdigest()
    for j in range(2016): # change to 0 for part 1
        initial = hashlib.md5((initial).encode('utf-8')).hexdigest()
    if i%100 == 0: print(i)
    m = re.findall(r'(\w)\1{2}',initial)
    if m:  threes.append((m[0],i))
    hashes.append(initial)

res = [index for three,index in threes if three*5 in ' '.join(hashes[index+1:index+1001]) ]
res[63]
# %%
