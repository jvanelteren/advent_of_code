#%%

# when working with a asyncio.queue, you don't need to await if you use put_nowait()
# prepare for the worst: literally ANY task can run during await


from asyncio.exceptions import CancelledError
from computerrefractored import Computer
import asyncio
noun, verb = 0,0
f=open('input.txt').read()
memory = tuple(int(i) for i in f.split(',')) # let's make it immutable as a tuple
memsize = 100000
memory = tuple(list(memory)+[0]*memsize)
send = 0
received = 0
class NicComputer(Computer):

    def __init__(self, *args,name=0):
        super().__init__(*args) 
        self.id = name
        self.queue = asyncio.Queue()
        self.writeidle, self.readidle  = 0,False

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
        # elif not self.queue.empty():
        #     toass = self.queue.get()
        #     self.input= toass
        #     # print('assigning queueu',toass,len(self.input))
        elif self.input[0] != -1:
            del self.input[0]
            return 'pauze'
        return 'pauze'
            

    async def runner(self):
        try:
            while True:
                if self.queue.empty(): self.readidle=True
                read = await self.queue.get()
                self.readidle=False
                # print('read'+str(self.id), read)
                self.input = read

                self.running = True
                self.process()
        except CancelledError:
            return 'cancelled'

    async def writer(self):
        try:
            while True:
                if True:
                    
                    for _ in range(5):
                        if not self.input:
                            self.input = [-1]
                        res = self.process()
                        if res:
                            self.writeidle += 1
                        else:
                            self.writeidle = 0
                        await asyncio.sleep(0.001)
        except CancelledError:
            return 'cancelled'
        
    def process(self):
        global natlast
        self.running = True
        in0 = self.runwait()

        if not in0:
            self.running = True
            in0 = self.runwait()

        if in0 and in0!='pauze':
            self.idle=False
            in1 = self.runwait()
            in2 = self.runwait()
            
            if in0 == 255:
                # print('setnatlast',in1,in2)
                natlast = (in1,in2)
            else:
                # print('sending'+str(self.id), (in0,in1,in2))
                nw[in0].readidle = False
                nw[in0].writeidle = 0


                nw[in0].queue.put_nowait([in1,in2])
        else:

            return True
            

natlast = (222,222)
resetlast = (111,111)
async def idle_checker():
    global natlast
    global resetlast
    while True:
        await asyncio.sleep(0.01)
        if all([c.writeidle > 2 for c in nw]) and all([c.readidle for c in nw]):
            print('IDLE DETECTED', natlast, resetlast)

            if natlast[1] == resetlast[1]:
                print('solution', natlast)
                for t in asyncio.all_tasks():
                    print (t.get_name())
                    if t.get_name().startswith('runner') or t.get_name().startswith('writer'):
                        t.cancel()
                
                return natlast
            else:
                # print('RESETTING')
                resetlast = natlast
                nw[0].writeidle = False
                nw[0].readidle = False
                nw[0].queue.put_nowait(list(resetlast))
        

#dont know if memory is a deep copy
nw = [NicComputer(list(memory),noun,verb,[i],name = i) for i in range(50)]
for c in nw:
    c.runwait()
    c.input = [-1]
    c.running = True

readers = [asyncio.create_task(c.runner(),name='runner'+str(i)) for i, c in enumerate(nw)]
writers = [asyncio.create_task(c.writer(),name='writer'+str(i)) for i, c in enumerate(nw)]

res = await asyncio.wait_for(asyncio.gather(*readers,*writers, idle_checker()),18)


# %%
res
# %%
