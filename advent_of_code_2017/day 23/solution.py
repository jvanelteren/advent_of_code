#%%
# read full assignment
# think algo before implementing
# dont use a dict when you need a list
# assignment is still = and not ==
# dont use itertools when you can use np.roll
# check mathemathical functions, e.g. if the parentheses are ok
# networkx is awesome
# sometimes while true is better than just too small for loop
# networkx addes nodes when adding edge to nonexistent node
# bitwise comparison is a nice trick
# fiddling with regex can take a lot of time
# insert on a list takes too much time when done often
# check the values from a dict or list after you set them
# check the input for edge cases
# implement very carefully, e.g. >0 instead of !=0
# day 23 was reverse engineering, took a lot of time. write down states of the program before tinkering with instructions

# %%
import os
import re
import numpy as np

try:
	os.chdir(os.path.join(os.getcwd(), 'day 23'))
	print(os.getcwd())
except:
	pass

# %%
f = open('input.txt','r')
ins = [[line.rstrip()[:3],line.rstrip()[4:5],line.rstrip()[6:]] for line in f]

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
        self.multip = 0
        self.reg['a']=1

    def receive(self,inp):
        self.q.put(inp)
        self.running = True

    def run(self):    
        c = 0
        self.done= []
        while self.running and c<200:
            # print(c,self.pos,self.reg)
            self.done.append((self.pos,ins[self.pos]))
            i = copy.deepcopy(ins[self.pos])
            if i[2] in self.reg.keys():
                i[2]= self.reg[i[2]]
            elif i[2]:
                i[2]=int(i[2])
            if i[0]=='snd': 
                self.lastsound = self.reg[i[1]]
                self.num_times_send+=1
                self.pos+=1
                return (self.lastsound,self.num_times_send)
            elif i[0]=='set':
                # set X Y sets register X to the value of Y.
                self.reg[i[1]] = i[2]
            elif i[0]=='sub':
                # sub X Y decreases register X by the value of Y.
                if i[1] == 'h':
                    if self.reg['f']==0:
                        self.reg[i[1]] -= i[2]
                else:
                        self.reg[i[1]] -= i[2]
            elif i[0]=='add':self.reg[i[1]] += i[2]
            elif i[0]=='mul':
                # mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
                self.reg[i[1]] *= i[2]
                self.multip += 1
            elif i[0]=='mod':self.reg[i[1]] = self.reg[i[1]] % i[2]
            elif i[0]=='rcv':
                if self.q.empty():
                    self.running = False
                    return None
                self.reg[i[1]] = self.q.get()
            elif i[0]=='jgz':
                if i[1]=='1' or self.reg[i[1]] > 0:
                    self.pos+= int(i[2])-1
            elif i[0]=='jnz':
                print(self.pos,self.reg)
                if i[1]=='1' or self.reg[i[1]] != 0:
                    if self.pos==14:
                        if is_prime(self.reg['b']):
                            self.pos+= int(i[2])-1
                    else:
                        self.pos+= int(i[2])-1
            self.pos+=1
            c+=1

prog0 = prog(0)
for _ in range(20000):
    res0 = prog0.run()
prog0.reg


# %%
import math
# checking for prime
def is_prime(n):
   # checking for less than 1
   if n <= 1:
      return False
   # checking for 2
   elif n == 2:
      return True
   elif n > 2 and n % 2 == 0:
      return False
   else:
      # iterating loop till square root of n
      for i in range(3, int(math.sqrt(n)) + 1, 2):
         # checking for factor
         if n % i == 0:
            # return False
            return False
      # returning True
      return True
# starting time
primes = 0
for i in range(108100,125100,17):
   if is_prime(i):
      primes += 1
print(f'Total primes in the range {primes}')
