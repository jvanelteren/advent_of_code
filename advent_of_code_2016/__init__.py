
# https://python-packaging.readthedocs.io/en/latest/minimal.html
# install with pip install -e .
#%%

from collections import namedtuple
def dimensions(obj): #gets an iterable of tuples and returns the minimums and maximums and ranges
    minim = tuple(min(obj,key = lambda x:x[i])[i] for i in range(len(obj[0])))
    maxim = tuple(max(obj,key = lambda x:x[i])[i] for i in range(len(obj[0])))# max for dimensions
    ranges = tuple(maxim[i] - minim[i]+1  for i in range(len(obj[0])))
    Dim = namedtuple('Dim',['min','max','range'])
    res = Dim(minim,maxim,ranges)
    return res

def normalize(*args): 
    """" takes 1 or multiple lists of n coordinates and returns it normalized (getting rid of negatives)

    """
    dtype = type(args[0][0]) # support list(s) of lists and list(s) of tuples
    if len(args)==1: # only 1 argument passed
        dim = dimensions(args[0])
        obj = args[0]
        if dtype == tuple:
            return [tuple(o[i]-dim.min[i] for i in range(len(obj[0]))) for o in obj]
        if dtype == list:
            return [[o[i]-dim.min[i] for i in range(len(obj[0]))] for o in obj]
        else: print('no support for dtype',dtype)
    else: # only multiple arguments passed
        dim = dimensions([i for a in args for i in a])
        if dtype == tuple:
            return ([tuple(o[i]-dim.min[i] for i in range(len(obj[0]))) for o in obj] for obj in args)

        if dtype == list: 
            return ([[o[i]-dim.min[i] for i in range(len(obj[0]))] for o in obj] for obj in args)
        else: print('no support for dtype',dtype)

def manhattan(x,y):
    return abs(x[0]-y[0])+abs(x[1]-y[1])

def neighbor2d(locations,i): #determine the neighbors from a list of locations
    res = []
    if (i[0],i[1]+1) in locations: res.append((i,(i[0],i[1]+1)))
    if (i[0],i[1]-1) in locations: res.append((i,(i[0],i[1]-1)))
    if (i[0]+1,i[1]) in locations: res.append((i,(i[0]+1,i[1])))
    if (i[0]-1,i[1]) in locations: res.append((i,(i[0]-1,i[1])))
    return res # list of tuples (input, neighbor)

def binarysearch(minim,maxim,function): #function needs to return a boolean whether the solution is ok
    while True:
        new = (minim+maxim)//2
        print(minim,maxim,new)
        if function(new):
            if new == maxim: # solution found
                print('solution found',new)
                return new
            maxim = new
        else: minim = new+1

from collections import deque
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

    while frontier:
        search = frontier.popleft()
        if isfunction: neighbors = connections(search)
        else: neighbors = connections.get(search,None)
        if neighbors:
            for n in neighbors:
                if n not in seen:
                    seen.add(n)
                    frontier.append(n)
                    # paths[n] = paths[search]+[n]
                    parents[n]= search
                    if goal and n == goal:
                        # print('goal found')
                        return get_path(parents,start,goal)
                        # return paths[goal],parents
        seen.add(search)
    if goal: return False
    else: return parents

import heapq
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

    def get_path(parents):
        cur = goal
        path = [cur]
        cost = parents[cur][1]
        while cur != start:
            cur = parents[cur][0]
            path.append(cur)
        path.reverse()
        return path,cost

    while frontier:
        # print('\n\n',frontier,'\n',parents)
        search_cost, search_node = heapq.heappop(frontier)
        # print('looking for', search_node,search_cost)
        if search_node == goal: break
        if isfunction: neighbors = connections(search_node)
        else: neighbors = connections.get(search_node,None)
        if neighbors:
            for n in neighbors:
                # print('n',n)
                if n[0] not in parents or n[1]+ search_cost < parents[n[0]][1]:
                    # print('updating')
                    heapq.heappush(frontier,(search_cost+n[1],n[0]))
                    # paths[n] = paths[search_node]+[n]
                    parents[n[0]]= (search_node,search_cost+n[1])
                        # return paths[goal],parents
        seen.add(search_node)
    if not goal: return parents
    elif goal in parents: return get_path(parents)
    else: return False

# found this on internet
def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited



# list(bfs_paths(graph, 'A', 'F')) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
class Pos():
    def __init__(self,input):
        self.x,self.y = input[0],input[1]
        self.loc = input
        self.n = getneigh((self.x,self.y))
        self.value = grid[input]
        self.door,self.key = False,False
        if self.value.isupper(): self.door = True
        elif self.value.islower(): self.key = True
    def enter(self,keys):
        if self.door:
            values = [(locations[k].value).upper() for k in keys]
            if self.value in values: return self.loc
            else: return False
        else: return self.loc
    def __repr__(self):
        return f'({self.x},{self.y}) {self.value} is door {self.door} is key {self.key}'


from math import sqrt
from functools import reduce
def factors(n):
        step = 2 if n%2 else 1
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

def flatten(S): # recusively flattens a list
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])

#%%
def ints(inp): # returns items converted to int if possible. also works for tuples
    if isinstance(inp[0],list):
        return [ints(l) for l in inp]
    if isinstance(inp[0],tuple):
        return tuple(ints(l) for l in inp)

    out = []
    for i in inp:
        try:
            out.append(int(i))
        except ValueError:
            out.append(i)
    if isinstance(inp,tuple): return tuple(out)
    else: return out

def neighbors1d(arr,conv_shape,mode='same',padding=None,pad_dir='center') ->list:
    """
    Returns a list of kernel views of a string or list 
    mode == 'valid': returns only results where the kernel fits
    mode == 'same': return the same amount of items as original
    when mode =='same', default padding is the outer value
    """
    if padding:
        to_pad = padding # user specified padding
    else:
        to_pad = arr[0] # begin or end of list

    if isinstance(arr,list): # to convert a list temporarily to string
        arr_is_list = True
    else:
        arr_is_list = False

    if mode == 'valid':
        pass

    p_size = conv_shape//2
    if mode == 'same':
        if arr_is_list:
            arr = ''.join(arr)
        if isinstance(arr,str): #here the padding is applied
            if pad_dir == 'center':
                arr = to_pad*p_size+arr+to_pad*p_size
            if pad_dir == 'left':
                arr = to_pad*(conv_shape-1)+arr
            if pad_dir == 'right':
                arr = arr+to_pad*(conv_shape-1)
        else:
            return 'only string and list supported'
        if arr_is_list:
            arr = list(arr)

    if conv_shape % 2 == 1: # odd conv_shape
        return [arr[i-p_size:i+p_size+1] for i in range(p_size,len(arr)-p_size)]
    else: # even conv_shape
        return [arr[i:i+conv_shape] for i in range(0,len(arr)-conv_shape+1)]

#%%
import numpy as np
def neighbors2d(arr,conv_shape,mode='same',padding=None,pad_dir='center') ->list:
    """
    Returns a list of kernel views of a string or list 
    mode == 'valid': returns only results where the kernel fits
    mode == 'same': return the same amount of items as original
    when mode =='same', default padding is the outer value
    """
    if padding:
        to_pad = padding # user specified padding
    else:
        to_pad = arr[0] # begin or end of list

    if isinstance(arr,list): # to convert a list to numpy array
        arr_is_list = True
    else:
        arr_is_list = False

    if mode == 'valid':
        pass

    p_size = conv_shape//2
    if mode == 'same':
        if arr_is_list:
            arr = np.array(arr)
        if isinstance(arr,str): #here the padding is applied
            if pad_dir == 'center':
                arr = to_pad*p_size+arr+to_pad*p_size
            if pad_dir == 'left':
                arr = to_pad*(conv_shape-1)+arr
            if pad_dir == 'right':
                arr = arr+to_pad*(conv_shape-1)
        else:
            return 'only string and list supported'
        if arr_is_list:
            arr = list(arr)

    if conv_shape % 2 == 1: # odd conv_shape
        return [arr[i-p_size:i+p_size+1] for i in range(p_size,len(arr)-p_size)]
    else: # even conv_shape
        return [arr[i:i+conv_shape] for i in range(0,len(arr)-conv_shape+1)]

# %%
import scipy, scipy.ndimage

def nb_vals(matrix, indices):
    matrix = scipy.array(matrix)
    indices = tuple(scipy.transpose(scipy.atleast_2d(indices)))
    arr_shape = scipy.shape(matrix)
    dist = scipy.ones(arr_shape)
    dist[indices] = 0
    dist = scipy.ndimage.distance_transform_cdt(dist, metric='chessboard')
    nb_indices = scipy.transpose(scipy.nonzero(dist == 1))
    return [matrix[tuple(ind)] for ind in nb_indices]

matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
nb_vals(matrix, [1,1])
import numpy as np
# %%
def neighbor2d(arr,radius=1):
    
    def neigh(indices):
        print (indices)
    for i in np.ndindex(arr.shape):
        neigh(i)

neighbor2d(np.arange(9).reshape(3,3))

# %%
test = np.arange(9).reshape(3,3)
a = np.array([[-1,0,1]])
a = np.repeat(a,3).reshape(3,3)
kernel = [np.array([v,a.T[i]]) for i,v in np.ndenumerate(a)]
neigh = [cell+[2,2] for cell in kernel]
cleanneigh = [n for n in neigh for i,v in enumerate(n) if test.shape[i]>v[i]>-1]
cleanneigh# %%

# %%
import numpy as np
def get_neighbors(arr):
    def getneigh(cell):
        x,y = cell
        return [arr[x2,y2] for x2 in range(x-1,x+2) for y2 in range(y-1,y+2) \
            if not (x2==x and y2==y) and -1<x2<arr.shape[0] and -1<y2<arr.shape[1]]
    res = arr.copy()
    for i in np.ndindex(arr.shape):
        res[i]=getneigh(i)
    return res
a = np.arange(9).reshape(3,3).astype(object)
print(a,a.shape)
n = (get_neighbors(a))

for i,v in np.ndenumerate(n):
    print(i,v)

# %%
import itertools
def get_neighbors(arr):
    options = [-1,0,1]
    options = combinations([options for _ in range(arr.ndim)])
    def getneigh(cell):
        x,y = cell
        return [arr[x2,y2] for x2 in range(x-1,x+2) for y2 in range(y-1,y+2) \
            if not (x2==x and y2==y) and -1<x2<arr.shape[0] and -1<y2<arr.shape[1]]
    res = arr.copy()
    for i in np.ndindex(arr.shape):
        res[i]=getneigh(i)
    return res
a = np.arange(9).reshape(3,3).astype(object)
print(a,a.shape)
n = (get_neighbors(a))
combin
# %%
import.itertools
# %%
a = []
a.
a.
# %%
