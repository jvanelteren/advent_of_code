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

# %%
f = open('input.txt','r')
ins = [line.rstrip().split(' ') for line in f]
# part1
reg = {'a':0,'b':0,'c':0,'d':0}
# part 2
reg = {'a':0,'b':0,'c':1,'d':0}

def solve():
    pos = 0
    while True:
        if pos>=len(ins):break
        i = ins[pos]
        if i[0]=='cpy':
            if i[1].isalpha():
                reg[i[2]] = reg[i[1]]
            else:
                reg[i[2]] = int(i[1])
        if i[0]=='inc': reg[i[1]]+=1
        if i[0]=='dec': reg[i[1]]-=1
        if i[0]=='jnz': 
            if i[1].isdigit() or reg[i[1]]!=0: pos += int(i[2])-1
        pos+=1
    return reg['a']


solve()

# %%
