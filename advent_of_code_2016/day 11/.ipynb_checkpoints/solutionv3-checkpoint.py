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
import re
from collections import Counter
import itertools

from string import ascii_lowercase,ascii_uppercase
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
                    parents[n.__repr__()]= search.__repr__()
                    if goal and n == goal:
                        print('goal found')
                        return get_path(parents)
                        # return paths[goal],parents
        seen.add(search.__repr__())
    print('done')
    if goal: return False
    else: return parents

class State(dict):
    def __init__(self,d):
        super().__init__(d)
        self.set_available()

    def __repr__(self):
        res = 'floor '+' floor '.join([v if v else 'none' for k,v in self.items()])
        return res

    def num_loose(self):
        res = ''.join([v if v else '' for k,v in self.items()])
        return int(len(re.findall('[a-zA-Z]',res))/2)

    def num_items(self):
        count = 0
        for i in range(4):
            count += int(self[i][0])*2
            count += len(self[i])-1
        if count == 14: return True
        else: return False

    def set_available(self):
        avail = []
        res = ''.join([v if v else '' for k,v in self.items() if k in [0,1,2,3]])
        for char in 'abcdefghi':
            if char not in res:
                avail.append(char)
        self.available = avail

    def recode(self):
        res = ''.join([v for k,v in self.items() if k in [0,1,2,3] and v])
        res = ''.join([c for c in res if c.isalpha() and c.islower()])
        code = ''.maketrans(res+res.upper(), ascii_lowercase[:len(res)]+ascii_uppercase[:len(res)])
        for k in self:
            if k in [0,1,2,3]:
                super().__setitem__(k,self[k].translate(code))
                self.set_available()

    def get_next_two_letters(self):
        return self.available[0:2]

    def __setitem__(self,k,v):
        if (k != 'elev' and v):
            v = ''.join(sorted(v))
            num_pairs = int(v[0])
            to_remove = [key for key,val in Counter(v.lower()).items() if val > 1]
            for i in to_remove: self.available.append(i)
            num_pairs+=len(to_remove)
            newstring = str(num_pairs)
            for i in v:
                if not i.lower() in to_remove and not i.isdigit():
                    newstring+=i
            super().__setitem__(k,newstring)
        else:
            super().__setitem__(k,v)

state = {0:'4', 1: '2A',2:'0a',3:'0','elev':'0'}
goal = {0:'0',1:'0',2:'0',3:'7','elev':'3'}

def isvalid(inp):
    for i in inp:
        if i.isalpha() and i.islower() and i.upper() not in inp:
            for j in inp:
                if (j.isdigit() and int(j)>0) or (j.isupper() and j.lower() != i): return False
    return True
nextfloor = {0:[1],1:[0,2],2:[1,3],3:[2]}

def getneigh(state):
    newstates = []
    cur_floor = int(state['elev'])
    next_two_letters = state.get_next_two_letters()
    current_floor = state[cur_floor] # used to be copy
    if int(current_floor[0])>0:
        current_floor+=next_two_letters[0].upper()+next_two_letters[0].lower()
        current_floor = str(int(current_floor[0])-1)+current_floor[1:]
    if int(current_floor[0])>0:
        current_floor+=next_two_letters[1].upper()+next_two_letters[1].lower()
        current_floor = str(int(current_floor[0])-1)+current_floor[1:]

    for comb in itertools.chain((itertools.combinations(current_floor[1:],2)), current_floor[1:]):
        comb = ''.join(comb)
        new_floor = ''.join([i for i in current_floor if i not in comb])
        if isvalid(comb) and isvalid(new_floor): # current floor is ok
            for n in nextfloor[cur_floor]:
                if isvalid(state[n] + comb): # new floor ok
                    newstate = State(state.copy())
                    newstate['elev']=str(n)
                    newstate[cur_floor] = new_floor
                    newstate[n] = newstate[n] + comb
                    newstate.recode()
                    assert newstate.num_items()
                    newstates.append(newstate)
    return newstates

a = State(state)
# %timeit for i in range(10): getneigh(a)
%load_ext line_profiler
%lprun -f getneigh getneigh(a)
# res = bfs(getneigh,State(state),State(goal))
# len(res)

# %%
1+1

# %%
