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
            99:(self.exit,0)}
        self.lastoutput='not set yet'
        self.running = True

    def receiveinput(self,i):
        self.input= [i]

    def restoregap(self):
        self.code[1] = self.noun
        self.code[2] = self.verb

    def summing(self,i,p):
        n = self.convert_to_param(i[:-1],p)
        self.code[self.imm(i[-1])] = n[0]+n[1]
    def multiply(self,i,p):
        n = self.convert_to_param(i[:-1],p)
        self.code[self.imm(i[-1])] = n[0]*n[1]
    def saveinput(self,i,p):
        # print('saveinput called',self.input)
        self.code[self.imm(i[-1])] = self.input[0]
        del self.input[0]
    def outputparam(self,i,p):
        n = self.convert_to_param(i,p)
        self.lastoutput = n
        # print('opcode 4 ',n)
        return n
    def jump_if_true(self,i,p):
        n = self.convert_to_param(i,p)
        if n[0] != 0: self.p = n[1]-3
    def jump_if_false(self,i,p):
        n = self.convert_to_param(i,p)
        if n[0] == 0: self.p = n[1]-3
    def less(self,i,p):
        n = self.convert_to_param(i[:-1],p)
        if n[0]<n[1]: self.code[self.imm(i[-1])] = 1
        else: self.code[self.imm(i[-1])] = 0
    def eq(self,i,p):
        n = self.convert_to_param(i[:-1],p)
        if n[0]==n[1]: self.code[self.imm(i[-1])] = 1
        else: self.code[self.imm(i[-1])] = 0
    def exit(self,i,p): print('should not be called')

    def analyze_opcode(self, val):
        op = val[-2:]
        parameters = val[-3::-1]
        return(op,parameters)
    def imm(self,x):return int(self.code[x])
    def par(self,x):return int(self.code[self.code[x]])
    def convert_to_param(self,ind,p):
        res = []
        for i in range(len(ind)):
            if i<len(p) and p[i]=='1': res.append(self.imm(ind[i]))
            else: res.append(self.par(ind[i]))
        res= [int(r) for r in res]
        return res

    def run(self):
        # self.restoregap() skip this step for day 5
        while self.running:
            try:
                op,parameters = self.analyze_opcode(str(self.code[self.p]))
                instruction, num_param = self.opcode[int(op)]
                if instruction == self.exit:
                    # print('code 99')
                    self.running = False
                    return
                indices = list(range(self.p+1, self.p+1+num_param))
                # print('ins',self.code[self.p],indices, num_param,instruction)
                if instruction == self.outputparam:
                    r = instruction(indices,parameters)
                    self.p += num_param+1
                    return r
                instruction(indices,parameters)
                self.p += num_param+1
            except Exception as e:
                print('error')
                return
        print('computer not running')
        return