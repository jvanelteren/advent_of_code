class Computer():
    def __init__(self,code, noun,verb, inputvalue):
        self.code, self.noun, self.verb, self.input, self.p = code, noun, verb, inputvalue, 0
        self.opcode = {
            1:(self.summing,3),
            2:(self.multiply,3),
            3:(self.saveinput,1),
            4:(self.outputparam,1),
            5:(self.jump_if_true,2),
            6:(self.jump_if_false,2),
            7:(self.less,3),
            8:(self.eq,3),
            9:(self.adjustrel,1),
            99:(self.exit,0)}
        self.lastoutput='not set yet'
        self.running = True
        self.relative = 0

    def read(self,x,mode):
        if mode == '0': return int(self.code[self.code[x]])
        elif mode == '1': return int(self.code[x])
        elif mode == '2': return int(self.code[self.code[x]+self.relative])
    def write(self,x,mode):
        if mode == '0': return self.code[x]
        elif mode == '2': return self.code[x]+self.relative
        elif mode == '1': return Exception
    def parametermodes(self,i,p):
        if len(p)<len(i): return p.ljust(len(i),'0')
        else: return p

    def receiveinput(self,i):
        self.input= [i]
        # print('input received',self.input[0])

    def restoregap(self):
        self.code[1] = self.noun
        self.code[2] = self.verb

    def summing(self,i,p):
        self.code[self.write(i[2],p[2])] = self.read(i[0],p[0]) + self.read(i[1],p[1])
    def multiply(self,i,p):
        self.code[self.write(i[2],p[2])] = self.read(i[0],p[0]) * self.read(i[1],p[1])
    def saveinput(self,i,p):
        self.code[self.write(i[0],p[0])] = self.input[0]
        # print('save input',self.input[0])
        del self.input[0]
        
    def outputparam(self,i,p):
        self.lastoutput = self.read(i[0],p[0])
        res = self.read(i[0],p[0])
        self.p += 2
        # print('out',res)
        return res
    def jump_if_true(self,i,p):
        if self.read(i[0],p[0]) != 0: self.p = self.read(i[1],p[1])-3
    def jump_if_false(self,i,p):
        if self.read(i[0],p[0]) == 0: self.p = self.read(i[1],p[1])-3
    def less(self,i,p):
        if self.read(i[0],p[0])<self.read(i[1],p[1]): self.code[self.write(i[2],p[2])]=1
        else: self.code[self.write(i[2],p[2])]=0
    def eq(self,i,p):
        if self.read(i[0],p[0])==self.read(i[1],p[1]): self.code[self.write(i[2],p[2])]=1
        else: self.code[self.write(i[2],p[2])]=0
    def adjustrel(self,i,p):
        self.relative += self.read(i[0],p[0])
    def exit(self,i,p):
        self.running = False
        print( 'opcode 99 computer finished')

    def run(self):
        # self.restoregap() skip this step for day 5
        while self.running:
            try:
                op = self.code[self.p] % 100
                instruction, num_param = self.opcode[op]
                parameters = str(self.code[self.p])[-3::-1]
                indices = [*range(self.p+1, self.p+1+num_param)]
                parameters = self.parametermodes(indices,parameters)
                res = instruction(indices,parameters)
                if res is not None: 
                    return res
                self.p += num_param+1
            except Exception as e:
                print('error',e)
                return
        return  'ending execution'