#%%
#  4, 6056, 6047, 3, 6056, 3, 6056]
magic = 30000
reg = {0:3,1:magic, 7:magic}
stack = []
def run():
    i = 0
    while i<1000000:
        
        i+=1
        if i % 100000 == 0:
            print(len(stack))
        if reg[0] != 0: #center 
            if reg[1] != 0:
                #jmp
                stack.append(reg[0])
                reg[1] -= 1
                stack.append(6056)
                continue
            else:
                reg[0] -= 1
                reg[1] = reg[7]
                stack.append(6047)
                continue
        else: #6027 reg0==0
            print(i)
            reg[0] = reg[1]+1
            if not stack:
                print('done, reg[0] should now be 6')
            # ret
            while stack[-1] != 6056:
                if stack[-1] == 6047: 
                    stack.pop()
                else:
                    print(stack[-1],'what to do')
                    sys.exit()
        
            reg[1]=reg[0]
            reg[0]=stack.pop()
            reg[0]-= 1
            stack.append(6067)
            continue
run()
# %%
1+1
# %%
