#%%
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
        print('\r', sep='\r',end='\r',flush=True)
    index += 1

# %%
for i in range(10):
    print(i,end='')
print('\r',end='')
for i in range(10):
    print(i,end='')

# %%
