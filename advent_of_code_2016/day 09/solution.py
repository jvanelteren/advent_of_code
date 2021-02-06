#%%
# always check the input carefully after opening and splitting
# split r and c indices for simplicity (instead of combining them into a tuple)
# when using re, be sure to thing if greedy or nongreedy parsing is necessary
# don't use re when split() suffices, whitespaces can be casted to int
# make sure to experiment with one item from a list instead of and immediate for loop
# when there is a clear test case available, test it!
# scan over the input a bit more carefully, it may be different than the test examples
# when plotting, use plt.imshow (not plt.show)
# i should look into itertools more
# %%
# initial solution, optimized in part 2
t = open('input.txt','r').read()
res = []
while t:
    char = t[0]
    if char == '(':
        close = t.find(')')
        i, number = map(int,t[1:close].split('x'))
        res.append(t[close+1:close+1+i]*number)
        t = t[close+1+i:]
    else:
        res.append(t[0])
        t = t[1:]
string = ''.join(res)
string = string.replace(' ','')
len(string)

# %%
# part 2
part2 = False
t = open('input.txt','r').read()
def decompress(t):
    res = 0
    while t:
        char = t[0]
        if char == '(':
            close = t.find(')')
            i, number = map(int,t[1:close].split('x'))
            to_append = t[close+1:close+1+i]
            if '(' in to_append and part2:
                res += decompress(to_append)*number
            else:
                to_append = ''.join(to_append).replace(' ','')
                res += len(to_append)*number
            t = t[close+1+i:]
        else:
            res+=1
            t = t[1:]
    return res
decompress(t)

# %%
