#%%
magic = 20
reg = {0:3,1:magic, 7:magic}
reg = {0:4,1:1, 7:magic}
stack = []
reg = {0:1,1:0, 7:2}
stack = [2,1,1]
def run():
    i = 0
    while i<10000000000:
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
                continue
        else: #6027 reg0==0
            reg[0] = reg[1]+1
            if not stack:
                print('done, reg[0] should now be 6',reg[0],reg[1])
            # ret
            while stack[-1] != 6056:
                if stack[-1] == 6047 or stack[-1] == 6067 : 
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

# MORE REDUCED VERSION WITHOUT THE STACK APPEND NOT NECESSARY
#%%
# 4, 6056, 6047, 3, 6056, 3, 6056, 3, 6056, 3, 6056, 3, 6056, 3, 6056, 3, 6056, 3, 6056, 3, 6056, 3, 6056, 3, 6056]
# 
magic = 2
reg = {0:3,1:magic, 7:magic}
reg = {0:1,1:0, 7:2}
stack = [4]

def run():
    while i<10000000000000:

        if reg[0] != 0: #center 
            if reg[1] != 0:
                stack.append(reg[0])
                reg[1] -= 1
                continue
            else:
                reg[0] -= 1
                reg[1] = reg[7]
                continue
        else: #6027 reg0==0
            reg[0] = reg[1]+1
            if not stack:
                print(reg[1])
                print('done, reg',reg[0],reg[1])
                break
            reg[1]=reg[0]
            reg[0]=stack.pop()
            reg[0]-= 1
            continue
run()


# %%

# COMPUTING THE REDUCTION 

results = {}
for magic in range(1,M):
 
    if magic % 100 == 0: print(magic)
    counts = {4:1,3:magic,2:magic,1:magic}
    # counts = {4:1,3:0,2:0,1:0}

    memo = {}

    M = 32768
    def compute(level, ones, magic, level_count):
        if (level,ones,magic,level_count) in memo: 
            return memo[(level,ones,magic,level_count)]
        
        if level == 2: 
            res = (ones + magic * level_count + level_count) % M
            memo[(level,ones,magic,level_count)] = res
            return res

        if level == 3:
            num_ones = ones
            #implementation good, but too slow because of the for loop
            for i in range(level_count):
                num_twos = compute(2,num_ones, magic, 1)
                num_ones = compute(2,magic, magic, num_twos)
            memo[(level,ones,magic,level_count)] = num_ones
            return num_ones
        if level == 4: # happens only once, no need for caching
            # implementation is ok since there is only 1 4 thank goodness
            num_threes = compute(2,ones, magic, level_count)
            return compute(3,magic, magic, num_threes)

    while True:
        counts = counts
        selected = False
        selected = 2 if counts[2] else 3 if counts[3] else 4 if counts[4] else False

        if not selected:
            results[magic] = counts[1]
            if (magic + counts[1] % M) == 5: print(magic)
            break
        if selected == 4:
            counts[4]=0
            counts[3]= compute(2,counts[1], magic, 1)
            counts[2]= magic
            counts[1]= magic
        else:
            counts[1] = compute(selected, counts[1],magic, counts[selected]) # only counts for reducting twos, for 3 works recursively?
            counts[selected] = 0

        
        # print(counts,adder)
# %%
magic = 2
num = 1
ones = 8
num = 38
ones = 2

ones + magic*num + num

# %%
[k for k, v in results.items() if (v + k ) % M == 5]
# 25734