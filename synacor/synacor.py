# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from aoc_utils import *
import tarfile
fname = 'synacor-challenge.tgz'
if fname.endswith("tar.gz"):
    tar = tarfile.open(fname, "r:gz")
elif fname.endswith("tar"):
    tar = tarfile.open(fname, "r:")
elif fname.endswith("tgz"):
    tar = tarfile.open(fname, "r:gz")
tar.extractall()
tar.close()


import numpy as np
# %%
f = open('challenge.bin', 'rb')
ins = np.fromfile(f, dtype=np.uint16)


class Comp():
    def __init__(self, ins, verbose=False):
        self.pnt = 0
        self.ins = ins
        self.functions = {
            0 : (self.halt,0,0),
            1 : (self.set,1,1),
            2 : (self.push,0,1),
            3 : (self.pop,1,0),
            4 : (self.eq,1,2),
            5 : (self.gt,1,2),
            6 : (self.jmp, 0,1),
            7 : (self.jt, 0,2),
            8 : (self.jf, 0,2),
            9 : (self.add, 1,2),
            10 : (self.mult, 1,2),
            11 : (self.mod, 1,2),
            12: (self.func_and, 1,2),
            13 : (self.func_or, 1,2),
            14 : (self.func_not, 1,1),
            15 : (self.rmem, 1,1),
            16 : (self.wmem, 0,2),
            17 : (self.call, 0,1),
            18 : (self.ret, 0,0),
            19: (self.out,0,1),
            20: (self.func_in,0,1),
            21: (self.noop,0,0),
        }
        self.M = 32768
        self.reg = {i:0 for i in range(8)}
        self.stack = []
        self.verbose = verbose


    def halt(self, args):
        #should not be called
        sys.exit()

    def set(self, args):
        self.reg[args[0]] = args[1]
        if self.verbose: print(f'reg {args[0]} is now {self.reg[args[0]]}')


    def push(self, args):
        #   push <a> onto the stack
        self.stack.append(args[0])
        if self.verbose: print('new stack', self.stack)

    def pop(self, args):
        top = self.stack.pop()
        self.reg[args[0]] = top
        if self.verbose: print('new stack', self.stack)
        

    def eq(self, args):
        #   set <a> to 1 if <b> is equal to <c>; set it to 0 otherwise
        a,b,c = args
        self.reg[a] = 1 if b == c else 0
        if self.verbose: print(f'reg {a} is now {self.reg[a]}')

    def gt(self, args):
        # set <a> to 1 if <b> is greater than <c>; set it to 0 otherwise
        a,b,c = args
        self.reg[a] = 1 if b > c else 0

    def jmp(self, args):
        return args[0]

    def jt(self, args):
        if args[0]:
            return args[1]

    def jf(self, args):
        if args[0] == 0:
            return args[1]

    def add(self, args):
        # assign into <a> the sum of <b> and <c> (modulo 32768)
        a, b, c = args
        self.reg[a] = (b + c) % self.M

    def mult(self, args):
        # assign into <a> the product of <b> and <c> (modulo 32768)
        a, b, c = args
        self.reg[a] = (b * c) % self.M

    def mod(self, args):
        # store into <a> the remainder of <b> divided by <c>
        a, b, c = args
        self.reg[a] = (b % c) % self.M

    def func_and(self, args):
        # stores into <a> the bitwise and of <b> and <c>
        a, b, c = args
        self.reg[a] = b & c

    def func_or(self, args):
        # stores into <a> the bitwise or of <b> and <c>
        a, b, c = args
        self.reg[a] = b | c

    def func_not(self, args):
        # stores 15-bit bitwise inverse of <b> in <a>
        a, b = args
        self.reg[a] = (~ b) % self.M

    def rmem(self, args):
        #   read memory at address <b> and write it to <a>
        a , b = args
        self.reg[a] = self.ins[b]

    def wmem(self, args):
        #   write the value from <b> into memory at address <a>
        a , b = args
        self.ins[a] = b

    def call(self, args):
        self.stack.append(self.pnt)
        return args[0]

    def ret(self, args):
        # remove the top element from the stack and jump to it; empty stack = halt
        return self.stack.pop()


    def out(self,args):
        print('out not implemented')
        sys.exit()
        print(chr(args[0]), end='')

    def func_in(self, args):
        print('get_in not implemented')
        sys.exit()

    def noop(self,args):
        pass


    def do_function(self, pnt):
        # read opcode
        opcode = self.ins[pnt]
        pnt += 1
        func, num_write, num_read = self.functions[opcode]
        if func == self.halt:
            return False
        # read arguments
        if self.verbose: print([ins[pnt+i] for i in range(num_write+num_read)])

        args = tuple(ins[pnt+i] % self.M for i in range(num_write))
        pnt += num_write
        args += tuple(ins[pnt+i] if ins[pnt+i] < 32768 else self.reg[ins[pnt+i] % self.M] for i in range(num_read))
        pnt += num_read
        self.pnt = pnt # needs to be updated for call to work
        if self.verbose: print(opcode, func.__name__, args)
        # optional: change pointer
        res = func(args)
        if res: # could do this with walrus
            if self.verbose: print('result', res)
            pnt = res
        # print(opcode, args, func, numargs, pnt)
        return pnt
    
    def run(self,amount=1000000000000000):
        for i in range(amount):
            self.pnt = self.do_function(self.pnt)
            if not self.pnt:
                print('ending')
                return

    
c = Comp(ins,verbose=False)
c.run(110000)
print('hi')
# %%