#%%
# read full assignment
# think algo before implementing
# dont use a dict when you need a list
# assignment is still = and not ==
# dont use itertools when you can use np.roll
# check mathemathical functions if the parentheses are ok
# networkx is awesome
# sometimes while true is better than just too small for loop
# networkx addes nodes when adding edge to nonexistent node
# bitwise comparison is a nice trick
# fiddling with regex can take a lot of time
# insert on a list takes too much time when done often
# check the values from a dict or list after you set them
# check the input for edge cases

# %%
import os
import re
import numpy as np

try:
	os.chdir(os.path.join(os.getcwd(), 'day 18'))
	print(os.getcwd())
except:
	pass

# %%
f = open('input.txt','r')
ins = [[line.rstrip()[:3],line.rstrip()[4:5],line.rstrip()[6:]] for line in f]
# %%

# %%
import copy
from queue import Queue
class prog():
    def __init__(self,ids):
        self.q = Queue()
        self.reg = {l[1]:0 for l in ins if l[1]!='1'}
        self.reg['p']= ids
        self.lastsound = 0
        self.num_times_send = 0
        self.pos = 0
        self.running = True

    def receive(self,inp):
        self.q.put(inp)
        self.running = True

    def run(self):    
        while self.running:
            i = copy.deepcopy(ins[self.pos])
            if i[2] in self.reg.keys():
                i[2]= self.reg[i[2]]
            elif i[2]:
                i[2]=int(i[2])
            if i[0]=='snd': 
                self.lastsound = self.reg[i[1]]
                print('snd',self.lastsound)
                self.num_times_send+=1
                self.pos+=1
                return (self.lastsound,self.num_times_send)
            elif i[0]=='set':
                self.reg[i[1]] = i[2]
            elif i[0]=='add':self.reg[i[1]] += i[2]
            elif i[0]=='mul':
                self.reg[i[1]] *= i[2]
            elif i[0]=='mod':self.reg[i[1]] = self.reg[i[1]] % i[2]
            elif i[0]=='rcv':
                if self.q.empty():
                    self.running = False
                    return None
                self.reg[i[1]] = self.q.get()
            elif i[0]=='jgz':
                if i[1]=='1' or self.reg[i[1]] > 0:
                    self.pos+= int(i[2])-1
            self.pos+=1

# %%
prog0 = prog(0)
prog1 = prog(1)
for _ in range(100000):
    res0 = prog0.run()
    if res0:
        prog1.receive(res0[0])
    res1 = prog1.run()
    if res1:
        prog0.receive(res1[0])
        print('res1 send',res1)
        

# %%
