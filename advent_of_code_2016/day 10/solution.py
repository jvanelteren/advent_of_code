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
# %%
f = open('input.txt','r')
lines = [line.rstrip().split(' ') for line in f]
print(f'len lines {len(lines)} first item {lines[0]}')

# %%
from collections import defaultdict
bots = defaultdict(list)
ins = defaultdict(list)

for line in lines:
    if line[0]=='value':
        bots[int(line[5])] = bots[int(line[5])]+[int(line[1])]
    if line[0]=='bot':
        # print(line[5],line[-2])
        if line[5]=='output':
            low = int(line[6])+1000
        else: low = line[6]
        if line[-2]=='output':
            high = int(line[-1])+1000
        else: high = line[-1]
        ins[int(line[1])] = [int(low),int(high)]

while True:
    if not [True for b,n in bots.items() if len(n)==2 and b<1000]: break
    full_bots = [(b,n) for b,n in bots.items() if len(n)==2 and b<1000]
    for bot, numbers in full_bots:
        bots[bot]=[]
        to_low, to_high = ins[bot]
        low,high = min(numbers),max(numbers)
        if low == 17 and high == 61:
            print('bot found!',bot)
        bots[to_low].append(low)
        bots[to_high].append(high)
    
bots[1000][0]*bots[1001][0]*bots[1002][0]

# %%
