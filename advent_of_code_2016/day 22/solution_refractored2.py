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
# use a class with __hash__ to store mutable objects

# %%
import re
from collections import namedtuple,deque,OrderedDict
import aoc
import numpy as np
import heapq
from copy import deepcopy

f = open('input.txt','r')
grid = np.zeros((35,29)).astype(object)
goal = (34,0)

lines = [line.rstrip().split(' ') for line in f]
for line in lines:
    val = []
    for item in line:
        if item and item[0] == r'/': 
            key = aoc.ints(re.findall(r'x(\d+)-y(\d+)',item)[0])
        if item and item[0].isdigit():
            val.append(int(item[:-1]))
    grid[key]=tuple(val[:2])

def neigh(arr): # initial neighbors, very slow so only 1 time
    def getneigh(cell):
        x,y = cell
        dif = [(0,1),(1,0),(-1,0),(0,-1)]
        return [(x+d[0],y+d[1]) for d in dif if -1<x+d[0]<arr.shape[0] and -1<y+d[1]<arr.shape[1]]
    res = arr.copy()
    for i in np.ndindex(arr.shape):
        res[i]=getneigh(i)
    return res

def getpairs(grid):
    pairs = set()
    for k,v in np.ndenumerate(grid):
        # print(k,v)
        for j,w in np.ndenumerate(grid):
            if k!=j and v[1] != 0 and v[1]<=w[0]-w[1] and abs(k[0]-j[0]) + abs(k[1]-j[1])<2:
                print('found',k,v)
                pairs.add((k,j))
    return tuple(pairs)

def newpairs(state):
    pairs = set()
    to_check = {p[0] for p in state.pairs} | {p[1] for p in state.pairs}
    for k in to_check:
        v = state.grid[k]
        for j in neighborcell[k]:
            w = state.grid[j]
            if k!=j and w[1] != 0 and w[1]<=v[0]-v[1]:
                pairs.add((j,k))
    state.pairs = pairs
    return state

def move(state,p):
    data_from = state.grid[p[0]]
    data_to = state.grid[p[1]]
    state.grid[p[1]] = (data_to[0], data_to[1]+data_from[1])
    state.grid[p[0]] = (data_from[0], 0)
    if p[0] == state.goal: # the goal has moved
        state.goal  = p[1]
    state = newpairs(state) # set the new pairs
    state.setempty() # set the empty square
    return state

def getneigh(state):
    newstate = []
    for p in state.pairs:
        newstate.append(move(deepcopy(state),p))
    return newstate

def a_star(connections,start, goal=None):
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
        return path,cost
    count= 0
    while frontier:
        search_cost, search_node = heapq.heappop(frontier)
        search_cost = parents[search_node][1]
        if count%10==0 : 
            print(f'looking for node {search_node}, cost {search_cost}')
        count+=1
        if isfunction: neighbors = connections(search_node)
        else: neighbors = connections.get(search_node,None)
        if neighbors:
            for n in neighbors:
                if n not in parents or 1+ search_cost < parents[n][1]:
                    heapq.heappush(frontier,(search_cost+1+n.distance,n))
                    parents[n]= (search_node,search_cost+1)
                    if n.goal == (0,0):
                        print ('found')
                        return len(get_path(parents,start,n)[0])-1
        seen.add(search_node)
    if not goal: return parents
    elif goal in parents: return get_path(parents)
    else: return False

class State():
    def setempty(self):
        self.empty = {p[1] for p in self.pairs}.pop()
    def __init__(self,grid,goal,pairs):
        self.grid = grid
        self.goal = goal
        self.pairs = pairs
        self.setempty()
    def __repr__(self): # for nicer printouts
        return str(self.goal) + str(self.empty)
    def __lt__(self, other): # to be able to heapq push (sorted list)
        return sum(self.goal) < sum(other.goal)
    def __eq__(self, other): # not completely sure why this is necessary
        return self.goal+self.empty == other.goal+other.empty
    def __hash__(self): # to be able to store the object in a set
        return hash(self.goal+self.empty)
    @property
    def distance(self): # for the A* heuristic
        return (sum(self.goal)-1)*5+aoc.manhattan(self.goal,self.empty)-1
        
start = State(grid,goal,getpairs(grid))
neighborcell = neigh(start.grid)
a_star(getneigh,start)


# %%
