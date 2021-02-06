#%%
# always check the input carefully after opening and splitting
# split r and c indices for simplicity (instead of combining them into a tuple)
# when using re, be sure to thing if greedy or nongreedy parsing is necessary
# don't use re when split() suffices, whitespaces can be casted to int
# make sure to experiment with one item from a list instead of and immediate for loop
# %%

import hashlib 

input = 'abc'
input = 'uqwqemis'

res = []
password = dict(zip(list(range(8)),[None]*8))
# encoding GeeksforGeeks using md5 hash 
while True:
    md5 = hashlib.md5((input+str(i)).encode()) 
    if md5.hexdigest()[:5]=='00000': 
        res.append(result.hexdigest())
        print(res[-1][5],res[-1][6])
        if len(res)==8: print(''.join([r[5] for r in res]))
        if not password.get(res[-1][5],99): 
            password[res[-1][5]]=res[-1][6]
            if sum([1 for v in password.values() if v])==7:
                print(password)
                break





# %%
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
 
import hashlib
import random
index = 0
password = '________'
while 1:
    m = hashlib.md5()
    m.update(('ugkcyxxp'+str(index)).encode('utf-8'))
    hex_m = m.hexdigest()
    if hex_m[0:5] == '00000':
        password_pos = int(hex_m[5], 16)
        if password_pos < 8:
            password_dig = int(hex_m[6], 16)
            if password[password_pos] == '_':
                password = password[:password_pos] + hex(password_dig)[-1] + password[password_pos + 1:]
    if index % 30000 == 0:
        for char in password:
            if char == '_':
                print(bcolors.HEADER + str(random.random())[-1] + bcolors.ENDC, end='')
            else:
                print(bcolors.OKGREEN + char + bcolors.ENDC, end='')
        print('\r', end='')
    index += 1

# %%
