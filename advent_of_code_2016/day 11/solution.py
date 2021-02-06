#%%
# always check the input carefully after opening and splitting
# split r and c indices for simplicity (instead of combining them into a tuple)
# when using re, be sure to thing if greedy or nongreedy parsing is necessary
# don't use re when split() suffices, whitespaces can be casted to int
# make sure to experiment with one item from a list instead of and immediate for loop
# !when there is a clear test case available, test it!
# scan over the input a bit more carefully, it may be different than the test examples
# when plotting, use plt.imshow (not plt.show)
# i should look into itertools more
# when refractoring a test case into the real code, check the indices are not hardcoded!
# use better descriptive names. also unpack if it makes code more readable for example in list of tuples
# with regex you can numbers pretty easily in a line. and -? to add possible negatives
# sometimes its easier to brute force bfs than to figure out an insane algo yourself

# %%
from collections import defaultdict
from collections import deque


# %%

def bfs(connections, start, goal=None):
    """
    Requires a dict with neighbors per node.
    Or a function returning neighbors per node

    Returns
    if goal == None:    return all paths from start
    elif goal found:    returns path to goal
    else:               returns False
    """
    seen = set() # the locations that have been explored
    frontier = deque([start]) # the locations that still need to be visited
    # paths = {start: [start]}
    isfunction = callable(connections)
    parents = {start.__repr__(): None}

    def get_path(parents):
        # print(start,goals)
        cur = goal.__repr__()
        path = [cur]
        while cur != start.__repr__():
            cur = parents[cur]
            path.append(cur)
        path.reverse()
        return path
    count = 0
    print(parents)
    while frontier:
        count+=1
        if count%1000 == 0:
            print(len(frontier),len(parents),len(seen))
            print(frontier[0])
        search = frontier.popleft()
        if isfunction: neighbors = connections(search)
        else: neighbors = connections.get(search,None)
        if neighbors:
            for n in neighbors:
                if n.__repr__() not in seen:
                    seen.add(n.__repr__())
                    frontier.append(n)
                    # paths[n] = paths[search]+[n]
                    parents[n.__repr__()]= search.__repr__()
                    if goal and n == goal:
                        # print('goal found')
                        return get_path(parents)
                        # return paths[goal],parents
        seen.add(search.__repr__())
    print('done')
    if goal: return False
    else: return parents

class State(dict):
    def __init__(self,d):
        super().__init__(d)

    def __repr__(self):
        
        res = 'floor '+' floor '.join([''.join(sorted(v)) if v else 'none' for k,v in self.items()])
        return res

state = {0:set('AaBbfFgG'), 1: set('CcDdE'),2:set('e'),3:set(),'elev':['0']}
goal = {0:set(),1:set(),2:set(),3:set(list('ABCDEFGabcdefg')),'elev':['3']}
import itertools
from itertools import chain
def isvalid(inp):
    for i in inp:
        if i.islower() and i.upper() not in inp:
            for j in inp:
                if j.isupper() and j.lower() != i: return False
    return True

nextfloor = {0:[1],1:[0,2],2:[1,3],3:[2]}

def getneigh(state):
    newstates = []
    cur_floor = int(state['elev'][0])
    for comb in chain((itertools.combinations(state[cur_floor],2)), state[cur_floor]):
        # print(comb)
        comb = set(comb)
        if isvalid(comb) and isvalid(state[cur_floor]-comb): # current floor is ok
            # print('go',state[cur_floor]-comb)
            for n in nextfloor[cur_floor]:
                if isvalid(state[n] | comb): # new floor ok
                    newstate = state.copy()
                    newstate['elev']=[str(n)]
                    newstate[cur_floor] = newstate[cur_floor] - comb #hele vage bug hier
                    newstate[n] = newstate[n] | comb
                    newstates.append(State(newstate))
                    # assert sum(len(v) for v in newstate.values() if v)==11
    return newstates

# getneigh(State(state))
# res = bfs(getneigh,State(state),State(goal))
# len(res)
# %%
import re
from collections import Counter
import itertools 
class State(dict):
    def __init__(self,d):
        super().__init__(d)

    def __repr__(self):
        
        res = 'floor '+' floor '.join([''.join(sorted(v)) if v else 'none' for k,v in self.items()])
        return res

    def num_loose(self):
        res = ''.join([''.join(sorted(v)) if v else '' for k,v in self.items()])
        return int(len(re.findall('[a-zA-Z]',res))/2)
    
    def get_next_two_letters(self):
        return 'abcdefg'[self.num_loose():self.num_loose()+2]

    def __setitem__(self,k,v):
        if k != 'elev' and v:
            v = ''.join(sorted(v))
            num_pairs = int(v[0])

            to_remove = [key for key,val in Counter(v.lower()).items() if val > 1]

            print('test',v,to_remove)
            num_pairs+=len(to_remove)
            newstring = str(num_pairs)
            for i in v:
                if not i.lower() in to_remove and not i.isdigit():
                    newstring+=i
        super().__setitem__(k,newstring)



state = {0:list('2'), 1: list('2A'),2:list('0a'),3:list('0'),'elev':['0']}
goal = {0:list('0'),1:list('0'),2:list('0'),3:list('7'),'elev':['3']}

def isvalid(inp):
    for i in inp:
        if i.isalpha() and i.islower() and i.upper() not in inp:
            for j in inp:
                if j.isdigit or j.isupper() and j.lower() != i: return False
    return True

nextfloor = {0:[1],1:[0,2],2:[1,3],3:[2]}

def getneigh(state):
    newstates = []
    cur_floor = int(state['elev'][0])
    next_two_letters = state.get_next_two_letters()
    current_floor = state[cur_floor]
    if int(current_floor[0])>0:
        current_floor+=next_two_letters[0].upper()+next_two_letters[0].lower()
    if int(current_floor[0])>1:
        current_floor+=next_two_letters[1].upper()+next_two_letters[1].lower()

    for comb in chain((itertools.combinations(current_floor[1:],2)), current_floor[1:]):
        # print(comb)
        comb = list(comb)
        print(comb)
        new_floor = [i for i in current_floor if i not in comb]
        if isvalid(comb) and isvalid(new_floor): # current floor is ok
            # print('go',state[cur_floor]-comb)

            for n in nextfloor[cur_floor]:
                if isvalid(state[n] + comb): # new floor ok
                    newstate = state.copy()
                    newstate['elev']=[str(n)]
                    newstate[cur_floor] = new_floor
                    newstate[n] = newstate[n] + comb
                    newstates.append(State(newstate))
                    # assert sum(len(v) for v in newstate.values() if v)==11
    return newstates
a = State(state)
getneigh(a)
# # getneigh(State(state))
# res = bfs(getneigh,State(state),State(goal))
# len(res)

# %%
state.__repr__()


# %%
import re
from collections import Counter
str = '1ABEabcd'
for i in 
# %%
v = '4aabbcc'
[key for key,val in Counter(v.lower()).items() if val > 1]

# %%
pat = re.compile(r'(\w).*\1')
pat.findall(r'1ABEabcdab')

# %%
