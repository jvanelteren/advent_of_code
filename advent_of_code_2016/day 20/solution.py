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
# use the easiest way to calculate solution (is set A is asked, dont calc set total - set B)
# %%
f = open('input.txt','r')
lines = [line.rstrip().split('-') for line in f]
blacklist = [tuple((int(l[0]),int(l[1]))) for l in lines]
blacklist.sort(key=lambda x: x[0])

pos,count = 0,0
part1 = True
for b in blacklist:
    if b[0]>pos:
        if part1: 
            print(pos)
            part1=False
        count += b[0]-pos
        pos = b[1]+1
    elif b[1]>pos:
        pos = b[1]+1
print(count)
