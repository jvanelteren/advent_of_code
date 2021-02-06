# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% De werkmap van de werkruimte root naar de ipynb-bestandslocatie veranderen. Schakel deze toevoeging uit met de instelling DataScience.changeDirOnImportExport
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'day 25'))
	print(os.getcwd())
except:
	pass
from IPython import get_ipython


# %%
from computerrefractored import Computer
noun, verb = 0,0
f=open('input.txt').read()
memory = tuple(int(i) for i in f.split(',')) # let's make it immutable as a tuple
memsize = 10000
memory = tuple(list(memory)+[0]*memsize)

def sendfunction(function):
    f = [ord(c) for c in list(function)]
    f.append(10)
    return f
    # c.receiveinput(res)

def runprogram(c,p):
    res = []
    for l in p:
        res = res+sendfunction(l)
    print('program to run', res)
    return res

def single():
    res = list('starting uppp')
    for x in range(500):
        r = c.run()
        if r:
            res.append(chr(r))
        if ''.join(res[-9:])=='Command?\n':
            print(''.join(res[16:]))
            return ''.join(res[16:])

def go(input,p=True):
    # print('Command given',input)
    c.receiveinput(sendfunction(input))
    res = list('starting uppp')
    for x in range(500):
        r = c.run()
        if r:
            res.append(chr(r))
        if ''.join(res[-9:])=='Command?\n':
            if p:
                print(''.join(res[16:]))
            return ''.join(res[16:])
            
def tryoption(c,ins):
    def go(input,p=False):
        # print('Command given',input)
        c.receiveinput(sendfunction(input))
        res = list('starting uppp')
        for x in range(300):
            r = c.run()
            if r:
                res.append(chr(r))
            if ''.join(res[-9:])=='Command?\n':
                if p:
                    print(''.join(res[16:]))
                return ''.join(res[16:])

    out = single()
    go('north') #arcade
    go('take sand')
    go('north') #observatory
    go('take space heater')
    go('east')
    go('take semiconductor')
    go('west')
    go('south')
    go('south')
    #main
    go('east')
    go('take ornament')
    #option east south split B south gedaan nu east
    go('south')
    go('take festive hat')
    #option east west --> east gedaan split A
    go('east')
    go('take asterisk')
    go('south') #stranded 50 stars needed
    #option east west --> east gedaan alleen nog west --> done
    go('west')
    go('take food ration')
    go('east')
    go('east') #nu east gedaan
    go('east')
    # go('take giant electromagnet') cannot move
    go('south')
    go('north')
    go('west')
    go('west')
    go('north')
    go('west')
    #split A nu west
    go('west')
    # go('take photons') dont take
    go('east')
    go('north')
    go('east')
    # go('take escape pod') #dont take
    go('east')
    go('west')
    go('west')
    go('west')

    # at the main again
    go('west')
    #option west north
    go('west')
    go('east')
    go('north')
    go('north')
    go('inv')

items = ['asterisk', 'ornament','space heater','festive hat','semiconductor','food ration', 'sand']

dropping = ['asterisk', 'food ration', 'sand']
c = Computer(list(memory),noun,verb,[])
tryoption(c,'a')
for t in dropping:
    go('drop'+' '+t)
print(testcase)

c.receiveinput(sendfunction('west'))
res = list('starting uppp')
for x in range(500):
    r = c.run()
    if isinstance(r,str):
        break
    if r:
        res.append(chr(r))
    if ''.join(res[-9:])=='Command?\n':
        if p:
            print(''.join(res[16:]))
print(''.join(res))
# go('west') # test room



# %%
import itertools
for L in range(0, len(items)+1):
    for testcase in itertools.combinations(items, L):

        c = Computer(list(memory),noun,verb,[])
        tryoption(c,'a')
        for t in testcase:
            go('drop'+' '+t)
        print(testcase)
        go('west')
        print(c.running)
    
# %%
c.receiveinput(sendfunction('west'))
res = list('starting uppp')
for x in range(500):
    r = c.run()
    if r:
        res.append(chr(r))
    if ''.join(res[-9:])=='Command?\n':
        print(''.join(res))
# go('drop sand')