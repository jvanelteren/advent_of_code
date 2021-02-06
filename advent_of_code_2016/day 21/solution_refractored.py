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
# when defining multiple functions, but an assert testcase below it that closely resembles input


# %%
import re
from collections import deque

f = open('input.txt','r')
lines = [line.rstrip() for line in f]

code = list('abcdefgh')
def swap_pos(code,swap):
    code[int(swap[0])],code[int(swap[1]) ]= code[int(swap[1])],code[int(swap[0])]
    return code

def swap_let(code,swap):
    swap[0] = code.index(swap[0])
    swap[1]= code.index(swap[1])
    code[(swap[0])],code[(swap[1]) ]= code[(swap[1])],code[(swap[0])]
    return code

def rotate(code, arg):
    print('rotate lr', code)
    code = deque(code)
    rot = int(arg[2])
    if arg[1]=='left':
        rot *=-1
    code.rotate(rot)
    print(arg[1],code)
    return list(code)

def rotate_let(code, arg):
    rot = code.index(arg[-1])+1
    if code.index(arg[-1])>=4: rot+=1
    code = deque(code)
    code.rotate(rot)
    return list(code)

def rev(code, arg):
    print(code)
    i = int(arg[2])
    j = int(arg[4])
    print(i,j)
    begin = []
    mid = []
    end = []
    if i>0: begin = code[0:i]
    mid = code[i:j+1][::-1]
    if j<len(code)-1: end = code[j+1:]
    print('mid',begin+mid+end)
    return begin+mid+end

def mov(code,arg):
    i = int(arg[2])
    j = int(arg[5])   
    letter = code[i]
    code.remove(letter)
    code.insert(j,letter)
    return code

for test in lines:
    print('ins',test,code, test[:12])
    if test[:6]=='swap p': code = swap_pos(code,re.findall(r'(\d)',''.join(test)))
    elif test[:6]=='swap l': code = swap_let(code,re.findall(r'letter (.)',''.join(test)))
    elif test[:12]=='rotate based': code = rotate_let(code,test.split(' '))
    elif test[:3]=='rot':code = rotate(code,test.split(' '))
    elif test[:3]=='rev': code = rev(code,test.split(' '))
    elif test[:3]=='mov': code = mov(code,test.split(' '))

# %%


f = open('input.txt','r')
lines = [line.rstrip() for line in f]
# print(f'len lines {len(lines)} first item {lines[0]}')
import re
code = list('fbgdceah')
# code = list('decab')
# code = list('abcde')
def swap_pos(code,swap):
    print('swappos',code,swap)
    code[int(swap[0])],code[int(swap[1]) ]= code[int(swap[1])],code[int(swap[0])]
    print(code)
    return code

def swap_let(code,swap):
    print(code,swap)
    swap[0] = code.index(swap[0])
    swap[1]= code.index(swap[1])
    print(swap)
    code[(swap[0])],code[(swap[1]) ]= code[(swap[1])],code[(swap[0])]
    print(code)
    return code

from collections import deque
def rotate(code, arg):
    print('rotate lr', code)
    code = deque(code)
    rot = int(arg[2])
    if arg[1]=='right':
        rot *=-1
    code.rotate(rot)
    print(arg[1],code)
    return list(code)

def rotate_let(code, arg):
    print('rotleft',code,code.index(arg[-1]) )
    rot = right[code.index(arg[-1])]
    code = deque(code)
    code.rotate(rot)
    print(code,rot)
    return list(code)

def rev(code, arg):
    print(code)
    i = int(arg[2])
    j = int(arg[4])
    print(i,j)
    begin = []
    mid = []
    end = []
    if i>0: begin = code[0:i]
    mid = code[i:j+1][::-1]
    if j<len(code)-1: end = code[j+1:]
    print('mid',begin+mid+end)
    return begin+mid+end

def mov(code,arg):
    print(code)
    i = int(arg[5])
    j = int(arg[2])   
    letter = code[i]
    
    code.remove(letter)
    code.insert(j,letter)
    return code

for test in lines[::-1]:
    print('ins',test,code, test[:12])
    if test[:6]=='swap p': code = swap_pos(code,re.findall(r'(\d)',''.join(test)))
    elif test[:6]=='swap l': code = swap_let(code,re.findall(r'letter (.)',''.join(test)))
    elif test[:12]=='rotate based': code = rotate_let(code,test.split(' '))
    elif test[:3]=='rot':code = rotate(code,test.split(' '))
    elif test[:3]=='rev': code = rev(code,test.split(' '))
    elif test[:3]=='mov': code = mov(code,test.split(' '))
''.join(code)
# %%
# left = {r: (r+r)%len(code)for r in range(8)}
right = {r: (r-((r-1)%len(code))%len(code)for r in range(8)}


# %%
def rotate_let(code, i):
    print('rotleft',code)
    rot = i+1
    if i >=4: rot+=1
    code = deque(code)
    code.rotate(rot)
    return (rot+i)%len(code)

initial = {i: rotate_let(list('01234567'),i) for i in range(8)}
right = {v: k-v for k,v in initial.items()}



# %%
initial = {i: rotate_let(list('01234'),i) for i in range(5)}
right = {v: k-v for k,v in initial.items()}

# %%
right

# %%
