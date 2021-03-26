# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from aoc_utils import *



# %%
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


# %%
import numpy as np
f = open('challenge.bin', 'rb')
ins = np.fromfile(f, dtype=np.uint16)


# %%
class Comp():
    def __init__(self, ins):
        self.pnt = 0
        self.ins = ins
        self.functions = {
            0 : (self.halt,0),
            1 : (self.set,2),
            2 : (self.push,1),
            3 : (self.pop,1),
            4 : (self.eq,3),
            5 : (self.gt,3),
            6 : (self.jmp, 1),
            7 : (self.jt, 2),
            8 : (self.jf, 2),
            9 : (self.add, 3),
            10 : (self.mult, 3),
            11 : (self.mod, 3),
            12: (self.func_and, 3),
            13 : (self.func_or, 3),
            14 : (self.func_not, 2),
            15 : (self.rmem, 2),
            16 : (self.wmem, 2),
            17 : (self.call, 1),
            18 : (self.ret, 18),
            19: (self.out,1),
            20: (self.func_in,1),
            21: (self.noop,0),
        }

    def halt(self, args):
        #should not be called
        sys.exit()

    def set(self, args):
        print('set not implemented')
        sys.exit()

    def push(self, args):
        print('push not implemented')
        sys.exit()

    def pop(self, args):
        print('pop not implemented')
        sys.exit()

    def eq(self, args):
        print('eq not implemented')
        sys.exit()

    def gt(self, args):
        print('gt not implemented')
        sys.exit()

    def jmp(self, args):
        return args[0]

    def jt(self, args):
        print('jt not implemented')
        sys.exit()
        
    def jf(self, args):
        print('jf not implemented')
        sys.exit()
        
    def add(self, args):
        print('add not implemented')
        sys.exit()

    def mult(self, args):
        print('mult not implemented')
        sys.exit()

    def mod(self, args):
        print('mod not implemented')
        sys.exit()

    def func_and(self, args):
        print('and not implemented')
        sys.exit()

    def func_or(self, args):
        print('or not implemented')
        sys.exit()

    def func_not(self, args):
        print('not not implemented')
        sys.exit()

    def rmem(self, args):
        print('rmem not implemented')
        sys.exit()

    def wmem(self, args):
        print('wmem not implemented')
        sys.exit()

    def call(self, args):
        print('call not implemented')
        sys.exit()

    def ret(self, args):
        print('ret not implemented')
        sys.exit()

    def out(self,args):
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
        func, numargs = self.functions[opcode]
        if func == self.halt:
            return False
        # read arguments
        args = tuple(ins[pnt+i] for i in range(numargs))
        pnt += numargs
        # optional: change pointer
        res = func(args)
        if res: # could do this with walrus
            pnt = res
        # print(opcode, args, func, numargs, pnt)
        return pnt
    
    def run(self,pnt, amount=1000000000000000):
        for i in range(amount):
            pnt = self.do_function(pnt)
            if not pnt:
                print('ending')
                return

    
c = Comp(ins)
c.run(0, 1100)


# %%
ins[:10]


# %%



