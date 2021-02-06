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
# sometimes its easier to brute force bfs than to figure out an insane algo yourself
# at beginning look at example first and highlighted texts
# utils for bfs make you really fast! boom place 13 on leaderboard
# try to bruteforce if not clear if you have to take a smart shortcut
# when checking if string appears in list of strings, be careful to use ' '.join not ''.join
# pay attention to parentheses when coding an condition, e.g. with mod
# pay attention to the types that you're using: [2929] != ['2929'] != list('2929') != [2,9,2,9]


# %%
def nextstate(inp):
    b = inp[::-1]
    c = ''.join(['0' if bb=='1' else '1' for bb in b])
    return inp+'0'+c
assert nextstate('111100001010') == '1111000010100101011110000'

# %%
def checksum(inp):
    res = ['1' if x==y else '0' for x,y in zip(inp[::2],inp[1::2])]
    # print(res)
    if len(res)%2 ==0: 
        return checksum(res)
    else: 
        return ''.join(res)
assert (checksum('110010110100')) == '100'

# %%
start = '10111011111001111'
des_len = 35651584
while len(start)<des_len:
    start = nextstate(start)
print('sol',checksum(start[:des_len]))
# %%