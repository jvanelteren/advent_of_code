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
# with assembly analysis make sure to print registers at important jump points


# %%
# part1
import math
reg = {'a':0,'b':0,'c':0,'d':0}
# part 2
reg = {'a':0,'b':0,'c':1,'d':0}
reg['a']=12
f = open('test0.txt','r')
ins = [line.rstrip().split(' ') for line in f]

def solve():
    pos = 0
    count = 0
    while True:
        count+=1
        if pos>=len(ins):break
        i = ins[pos]
        if i[0]=='cpy':
            if i[1].isalpha():
                reg[i[2]] = reg[i[1]]
            else:
                reg[i[2]] = int(i[1])
            
        if i[0]=='inc': 
            reg[i[1]]+=1
        if i[0]=='dec': reg[i[1]]-=1
        if i[0]=='jnz': 
            if (i[1].isdigit() and int(i[1]) != 0) or reg[i[1]]!=0: 
                if i[2].isalpha():
                    pos += reg[i[2]]-1
                else:
                    pos += int(i[2])-1
        if i[0]=='tgl':
            if i[1].isalpha():
                temppos = pos + reg[i[1]]
            else:
                temppos = pos + int(i[1])
            if 0 <= temppos <len(ins):
                curins = ins[temppos][0]
                if curins == 'inc': ins[temppos][0]='dec'
                elif curins == 'dec': ins[temppos][0]='inc'
                elif curins == 'cpy': ins[temppos][0]='jnz'
                elif curins == 'jnz': ins[temppos][0]='cpy'
                elif curins == 'tgl': ins[temppos][0]='inc'
        pos+=1
    return reg['a']

large = math.factorial(12)
reg['d']=large
reg['c']=0
reg['b']=0
reg['a']=large

solve()
