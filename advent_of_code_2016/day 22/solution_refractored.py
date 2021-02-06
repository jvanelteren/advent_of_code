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
# use the easiest way to calculate solution (is set A is asked, dont calc set total - set B)
# when defining multiple functions, but an assert testcase below it that closely resembles input


# %%
import re
from collections import namedtuple,deque,OrderedDict
import aoc
f = open('input.txt','r')
lines = [line.rstrip().split(' ') for line in f]
direc = OrderedDict()
for line in lines:
    val = []
    for item in line:
        
        if item and item[0] == r'/': 
            # print(re.findall(r'x(\d+)-y(\d+)',item))
            key = aoc.ints(re.findall(r'x(\d+)-y(\d+)',item)[0])
        if item and item[0].isdigit():
            val.append(int(item[:-1]))
    direc[key]=val
state=namedtuple('State', ['size', 'used', 'avail'])
for key in direc:
    init = direc[key]
    direc[key]=state(init[0],init[1],init[2])
direc[(99,99)] = (34,0)
# direc[(99,99)] = (2,0)
class Status():
    def __init__(self,direc):
        self.direc = direc
    def __repr__(self):
        return str(self.direc.values())

def getpairs(direc):
    pairs = set()
    for k,v in direc.direc.items():
        for j,w in direc.direc.items():
            if k != (99,99) and j != (99,99) and k!=j and v.used!=0 and v.used<=w.avail and abs(k[0]-j[0]) + abs(k[1]-j[1])<2:
                # print('pair found',k,j)
                pairs.add((k,j))
    return pairs


def move(direc,p):

    direc.direc[p[1]] = state(direc.direc[p[1]].size, direc.direc[p[1]].used+direc.direc[p[0]].used,direc.direc[p[1]].avail-direc.direc[p[0]].used)
    direc.direc[p[0]] = state(direc.direc[p[0]].size, 0 , direc.direc[p[0]].size )

    return direc  

from copy import deepcopy
def getneigh(direc):
    pairs = getpairs(direc)
    newstate = []
    # print(pairs)
    for p in pairs:
        newstate.append(move(deepcopy(direc),p))
        # print(newstate[-1].direc)
        if p[0] == newstate[-1].direc[(99,99)]:
            # print('goal moved to',p[1])
            newstate[-1].direc[(99,99)]=p[1]
    # print(len(newstate))
    return newstate

direc = Status(direc)   
a = getneigh(direc) 
for i in a: getneigh(i) 
#%%

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
    parents = {start: None}

    def get_path(parents,start,goal):
        # print(start,goals)
        cur = goal
        path = [cur]
        while cur != start:
            cur = parents[cur]
            path.append(cur)
        path.reverse()
        return path
    count = 0
    while frontier:
        if count %1000 ==0: print(len(frontier),len(parents))
        search = frontier.popleft()
        if isfunction: neighbors = connections(search)
        else: neighbors = connections.get(search,None)
        if neighbors:
            # print(len(neighbors))
            for n in neighbors:
                if n not in seen:
                    seen.add(n)
                    frontier.append(n)
                    # paths[n] = paths[search]+[n]
                    parents[n]= search
                    # print(n.direc[(99,99)])
                    if n.direc[(99,99)]==(0,0):
                        print('found')
                        return get_path(parents,start,n)
                        # return paths[goal],parents
        seen.add(search)
    if goal: return False
    else: 
        print('notfound')
        return parents
res = bfs(getneigh,direc)
print(len(res))


def distance(state):
    return sum(state.direc[(99,99)])
# %%
# 1679 too high
def dijkstra(connections,start, goal=None):
    """
    Requires a dict with as values a LIST of tuples (neighbor, weight)
    Or a function returning a list of tuples with neighbors and weights per node

    Returns
    if goal == None:    return all paths from start
    elif goal found:    returns path to goal
    else:               returns False
    """
    seen = set() # the locations that have been explored
    frontier = [(0,start)] # the locations that still need to be visited
    isfunction = callable(connections)
    parents = {start: (None,0)}

    def get_path(parents,start,goal):
        cur = goal
        path = [cur]
        cost = parents[cur][1]
        while cur != start:
            cur = parents[cur][0]
            path.append(cur)
        path.reverse()
        print(len(path))
        return path,cost


    count = 0
    while frontier:
        count+=1
        if count %100==0:
            print('\n\n',len(frontier),'\n',len(parents))
        search_cost, search_node = heapq.heappop(frontier)
        # print('looking for', search_node,search_cost)
        if search_node == goal: break
        if isfunction: neighbors = connections(search_node)
        else: neighbors = connections.get(search_node,None)
        if neighbors:
            # print(len(neighbors))
            for n in neighbors:
                if n not in parents or 1+ search_cost < parents[n][1]:
                    # print('updating')
                    heapq.heappush(frontier,(search_cost+1,n))
                    # paths[n] = paths[search_node]+[n]
                    parents[n]= search_node,search_cost+1
                    # print(n[0][-1])
                    if n.direc[(99,99)]==(0,0): 
                        print('found')
                        return get_path(parents,start,n)
        seen.add(search_node)
    if not goal: return parents
    elif goal in parents: return get_path(parents)
    else: return False
import heapq
dijkstra(getneigh,direc)

# %%
