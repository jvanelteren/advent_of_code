import sys
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

    def receiveinput(self,i):
        self.input= [i]

    def restoregap(self):
        self.code[1] = self.noun
        self.code[2] = self.verb
    def save_to_target(self,res, i,p):
        if p[0] == '2': 
            #print(f"setting memory no {i[0]+self.relative} to {self.input[0]} which was previously{self.code[i[0]+self.relative]}")
            self.code[self.code[i]+self.relative]= res
        elif p[0] == '1': sys.exit()
        else: self.code[self.code[i]]= res

    def summing(self,i,p):
        n = self.convert_to_param(i[:-1],p)
        if len(p)>2: p = p[2]
        else: p = '0'
        self.save_to_target(n[0]+n[1], i[-1],p)
    def multiply(self,i,p):
        n = self.convert_to_param(i[:-1],p)
        if len(p)>2: p = p[2]
        else: p = '0'
        self.save_to_target(n[0]*n[1], i[-1],p)
    def saveinput(self,i,p):
        n = self.convert_to_param(i,p)
        #print('saveinput called',i,'p',p,'input',self.input[0],'relative',self.relative, 'outconvert', n[0], 'immediate',self.imm(i[0]))
        self.save_to_target(self.input[0], i[0],p)
        del self.input[0]
    def outputparam(self,i,p):
        n = self.convert_to_param(i,p)
        self.lastoutput = n
        #print('opcode 4 ',n)
        return n
    def jump_if_true(self,i,p):
        n = self.convert_to_param(i,p)
        if n[0] != 0: self.p = n[1]-3
    def jump_if_false(self,i,p):
        n = self.convert_to_param(i,p)
        if n[0] == 0: self.p = n[1]-3
    def less(self,i,p):
        n = self.convert_to_param(i[:-1],p)
        #print(p)
        if len(p)>2: p = p[2]
        else: p = '0'
        if n[0]<n[1]: self.save_to_target(1, i[-1],p)
        else: self.save_to_target(0, i[-1],p)
    def eq(self,i,p):
        n = self.convert_to_param(i[:-1],p)
        if len(p)>2: p = p[2]
        else: p = '0'
        if n[0]==n[1]: self.save_to_target(1, i[-1],p)
        else: self.save_to_target(0, i[-1],p)
    def adjustrel(self,i,p):
        #print('adjust relative mode',self.relative)
        n = self.convert_to_param(i,p)
        self.relative += n[0]
        #print(self.relative)
    def exit(self,i,p): print('should not be called')

    def analyze_opcode(self, val):
        op = val[-2:]
        parameters = val[-3::-1]
        return(op,parameters)
    def imm(self,x):return int(self.code[x])
    def par(self,x):return int(self.code[self.code[x]])
    def rel(self,x):
        #print('relative mode lookup',self.relative, 'and',x)
        return int(self.code[self.code[x]+self.relative])
    def convert_to_param(self,ind,p):
        res = []
        for i in range(len(ind)):
            if i<len(p) and p[i]=='1': 
                # print('converting to immediate')
                res.append(self.imm(ind[i]))
            elif i<len(p) and p[i]=='2': 
                #print('converting to relative')
                res.append(self.rel(ind[i]))
                #print('result conversion',self.rel(ind[i]) )
            else: 
                # print('converting to parameter')
                res.append(self.par(ind[i]))
        res= [int(r) for r in res]
        return res

    def run(self):
        # self.restoregap() skip this step for day 5
        while self.running:
            try:
                op,parameters = self.analyze_opcode(str(self.code[self.p]))
                instruction, num_param = self.opcode[int(op)]
                if instruction == self.exit:
                    print('code 99')
                    self.running = False
                    return
                indices = list(range(self.p+1, self.p+1+num_param))
                #print('ins',self.code[self.p],indices, num_param,instruction)
                if instruction == self.outputparam:
                    r = instruction(indices,parameters)
                    self.p += num_param+1
                    return r
                instruction(indices,parameters)
                self.p += num_param+1
            except Exception as e:
                print('error',e)
                return
        print('computer not running')
        return