# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% De werkmap van de werkruimte root naar de ipynb-bestandslocatie veranderen. Schakel deze toevoeging uit met de instelling DataScience.changeDirOnImportExport
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'day 23'))
	print(os.getcwd())
except:
	pass
# %%



# %%
#tried to develop this one in the VSCode interactive environment

from computerrefractored import Computer
import string
import queue 
noun, verb = 0,0
f=open('input.txt').read()
memory = tuple(int(i) for i in f.split(',')) # let's make it immutable as a tuple
memsize = 100000
memory = tuple(list(memory)+[0]*memsize)

class NicComputer(Computer):
    def __init__(self, *args,name=0):
        super().__init__(*args) 
        self.id = name
        self.queue = queue.Queue()
    def runwait(self):
        # self.restoregap() skip this step for day 5
        while self.running:
            try:
                op = self.code[self.p] % 100
                instruction, num_param = self.opcode[op]
                parameters = str(self.code[self.p])[-3::-1]
                indices = [*range(self.p+1, self.p+1+num_param)]
                parameters = self.parametermodes(indices,parameters)
                res = instruction(indices,parameters)
                if res is not None and res != 'pauze': 
                    return res
                self.p += num_param+1
                if not self.input: 
                    self.running = False
                if res == 'pauze':
                    return
            except Exception as e:
                print('error',e)
                return
        return
    def saveinput(self,i,p):
        self.code[self.write(i[0],p[0])] = self.input[0]
        if len(self.input)>1:
            del self.input[0]
        elif not self.queue.empty():
            toass = self.queue.get()
            # print('read'+str(c.id), toass)
            self.input= toass
        elif self.input[0] != -1:
            del self.input[0]
            return 'pauze'
        else:
            del self.input[0]
            return 'pauze'
#dont know if memory is a deep copy
nw = [NicComputer(list(memory),noun,verb,[i],name = i) for i in range(50)]
for c in nw:
    c.runwait()
    c.input = [-1]
    c.running = True
# %%
nat = 'init'
resy = 99999
# all([not c.running for c in nw])
totalwrite = 0
totalread=0
while True:
    if all([c.queue.empty() for c in nw]) and nat != 'init' and all([not c.input for c in nw]) and all([not c.running for c in nw]):
        print('nat',nat)
        nw[0].queue.put([nat[0],nat[1]])
        if nat[1]==resy:
            print('DONE',nat[1])
            sys.exit()
        else: resy = nat[1]



    for c in nw:
        for i in range(100):
        # print(c.id)
        # c.input = [-1]
            c.running = True
            if not c.input:
                if c.queue.empty():
                    c.input=[-1]
                else:
                    toass = c.queue.get()
                    # print('read'+str(c.id), toass)
                    totalread += 1
                    c.input= toass
            in0 = c.runwait()
            if in0 and in0!='pauze':
                in1 = c.runwait()
                in2 = c.runwait()
                # print((in0,in1,in2))
                
                if in0 == 255:
                    # print('found 255',c.id, in1,'y',in2)
                    nat = [in1,in2]
                else:
                    if in0==15:
                        print(' 15 add',in1,in2)
                    nw[in0].queue.put([in1,in2])
                    # print('sending'+str(c.id), (in0,in1,in2))
                    totalwrite+=1
                    # print('totalwrite', totalwrite)
                    
#%%
        

# %%
