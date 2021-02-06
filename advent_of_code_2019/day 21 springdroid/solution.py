# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% De werkmap van de werkruimte root naar de ipynb-bestandslocatie veranderen. Schakel deze toevoeging uit met de instelling DataScience.changeDirOnImportExport
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'day 21'))
	print(os.getcwd())
except:
	pass
# %%
from IPython import get_ipython


# %%
#tried to develop this one in the VSCode interactive environment
import numpy as np
import matplotlib.pyplot as plt
from computerrefractored import Computer
import string

def sendfunction(function):
    res =[]
    for i in function:
        f = [ord(c) for c in list(i)]
        res.extend(f)
        res.append(ord(' '))
    res = res[:-1]
    res.append(10)
    return res

def runprogram(c,p):
    res = []
    for l in p:
        res = res+sendfunction(l)
    # c.receiveinput(res)
    print('program to run', res)
    return res

def getview(c):
    lines = []
    line = []
    while c.running:
        line.append(int(c.run()))
        if line[-9:]==[97,99,114,111,115,115, 58, 10, 10]:
            line = []
            print('start print')
            break
    while c.running:
        char = c.run()
        if char =='ending execution':
            print('end detected')
            view = np.array(lines)
            print(view)
            return view
        if char == 10:
            if len(line)!=0:
                lines.append(line[:20])
                line = []
        else:
            line.append(chr(char))
# %%
noun, verb = 0,0
f=open('input.txt').read()
memory = tuple(int(i) for i in f.split(',')) # let's make it immutable as a tuple
memsize = 10000
memory = tuple(list(memory)+[0]*memsize)

program1 = [
['NOT','B','T'],
['NOT','C','J'],
['OR','J','T'],
['NOT','A','J'],
['AND','D','J'],
['AND','D','T'],
['OR','T','J'],
['WALK']]

program2 = [
['OR','E','T'],
['OR','H','T'],
['NOT','C','J'],
['AND','J','T'],
['NOT','B','J'],
['OR','J','T'],
['NOT','A','J'],
['AND','D','J'],
['AND','D','T'],
['OR','T','J'],
['RUN']]

print('part 1\n')
c = Computer(list(memory),noun,verb,[])
c.receiveinput(runprogram(c,program1))
for i in range(1000):
    res = c.run()
    print(c.run())
    if res == 'ending execution': break

print('part 2')
c = Computer(list(memory),noun,verb,[])
c.receiveinput(runprogram(c,program2))
for i in range(1000):
    res = c.run()
    print(c.run())
    if res == 'ending execution': break

# %%
# this part I wrote to test my program a bit more friendly than the intcomputer
def iand(x,y):
    return x*y
def inot(x,y):
    if x==0: return 1
    else: return 0
def ior(x,y):
    if x+y>0: return 1
    else: return 0

def runner(init,ins):
    mem = {}
    #memory for the first nine letters
    mem = {string.ascii_uppercase[c] : init[c] for c in range(0,9)}
    mem['T']=0
    mem['J']=0
    for i in ins:
        mem[i[2]] = i[0](mem[i[1]],mem[i[2]])
    return mem

tests = [
([1,0,0,0,1,1,1,1,1],0,'dont jump if D 0 and A 1'),
([1,1,1,0,1,1,1,1,1],0,'dont jump if D 0 and A 1'),
([1,1,0,0,1,1,1,1,1],0,'dont jump if D 0 and A 1'),
([1,0,1,0,1,1,1,1,1],0,'dont jump if D 0 and A 1'),
([0,0,0,1,1,1,1,1,1],1,'jump if A 0 and D 1'),
([0,0,0,1,1,1,1,1,1],1,'jump if A 0 and D 1'),
([0,0,0,1,1,1,1,1,1],1,'jump if A 0 and D 1'),
([0,0,0,1,1,1,1,1,1],1,'jump if A 0 and D 1'),

([1,1,0,1,0,1,0,0,0],0,'dont jump if C is 0, but dead later'),
([1,1,0,1,0,0,1,1,1],1,'jump if C is 0, not dead later'),
([1,1,0,1,0,1,0,1,1],1,'jump if A D 1 and C is 0'),
([1,1,0,1,1,1,0,0,0],1,'jump if A D 1 and C is 0'),
([1,0,1,1,1,1,1,1,1],1,'jump if A D 1 and B is 0',),
([1,0,0,1,1,1,1,1,1],1,'jump if holes in B and C'),
([1,0,0,1,1,1,1,1,1],1,'not defined yet'),
([1,0,0,1,1,1,1,1,1],2,'success!')
# not testing scenario where A 0 and D 0
]
# %%]
ins = [ # the instructions to be tested
    [ior,'E','T'],
    [ior,'H','T'],
    [inot,'C','J'],
    [iand,'J','T'],
    [inot,'B','J'],
    [ior,'J','T'],
    [inot,'A','J'],
    [iand,'D','J'],
    [iand,'D','T'],
    [ior,'T','J']
]

for test in tests: # run all assertion tests
    res = runner(test[0],ins)
    print ('test',test,'memory',res.values())
    assert res['J']==test[1]
