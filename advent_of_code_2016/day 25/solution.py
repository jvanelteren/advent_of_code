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
# use the easiest way to calculate solution (is set A is asked, dont calc set total - set B)
# when defining multiple functions, but an assert testcase below it that closely resembles input
# use a class with __hash__ to store mutable objects
# with assembly analysis make sure to print registers at important jump points
# don't implement an algo if you are pretty sure it isnt going to work
# assembly analysis is not very easy

# %%

import math

f = open('input.txt','r')
ins = [line.rstrip().split(' ') for line in f]

def solve(i):
    reg = {'a':i,'b':0,'c':0,'d':0}
    pos = 0
    count = 0
    out = []
    while len(out)<20 and count<10000000:
        count+=1
        if pos>=len(ins):break
        i = ins[pos]
        if i[0]=='cpy':
            if i[1].isalpha():
                reg[i[2]] = reg[i[1]]
            else:
                reg[i[2]] = int(i[1])
        if i[0]=='out':
            out.append(reg[i[1]])
        if i[0]=='inc': 
            reg[i[1]]+=1
        if i[0]=='dec': reg[i[1]]-=1
        if i[0]=='jnz': 
            if (i[1].isdigit() and int(i[1]) != 0) or (i[1].isalpha() and reg[i[1]]!=0): 
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
    return out

for i in range(180,8000,1):
    res = solve(i)
    if i%100==0: print(i)
    if all([i !=j for i,j in zip(res,res[1:])]):
        print('solution found',i, res)
        break

# %%
for i in range(10):
    reg = {'a':0,'b':0,'c':0,'d':0}
    reg['a']=i
    reg['b']=reg['a']
    reg['a']=0
    reg['c']=2
    while reg['b']!=0:
        reg['b']-=1
        reg['c']-=1
        if reg['c']==0: 
            reg['a']+=1
            reg['c']=2
    print(i, reg)
b = a
a = 0
while true {
  c = 2
  do {
    if b == 0 {
      jump to block C
    }
    b--
    c--
  } while c != 0
  a++
}

# %%
out = 1
while out < 14*182/2:
    out = out * 2 
    print(out)
    out = out * 2+1
    print(out)

# %%
