from collections import namedtuple
import queue
from collections import defaultdict

def dimensions(obj): #gets an iterable of tuples and returns the minimums and maximums and ranges
    minim = tuple(min(obj,key = lambda x:x[i])[i] for i in range(len(obj[0])))
    maxim = tuple(max(obj,key = lambda x:x[i])[i] for i in range(len(obj[0])))# max for dimensions
    ranges = tuple(maxim[i] - minim[i]+1  for i in range(len(obj[0])))
    Dim = namedtuple('Dim',['min','max','range'])
    res = Dim(minim,maxim,ranges)
    return res

def normalize(*args): #takes 1 or multiple lists of n coordinates and returns it normalized (getting rid of negatives)
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


def bfs(edges,start=(0,0),goal=None): #does a breath first search, e.g. to find shortest path from start to goal
    paths = defaultdict(list) #dictionary with steps from start to key. Maybe not always necessary
    to_visit = queue.Queue() # the locations that still need to be visited
    to_visit.put(start) # first location is start
    visited = set([start]) # the locations that have been explored
    children = defaultdict(list)
    while not to_visit.empty():
        vertex = to_visit.get()
        current_path = paths[vertex]
        # print('\nvertex',vertex,'current_path',current_path)
        if vertex == goal:
            print( 'finished')
            return (visited,paths)
        p,ed = edges(current_path,vertex) #receive the step needed to go to the next location
        for i,e in enumerate(ed):
            if e not in visited:
                paths[e]=current_path+[p[i]] # make a path how to reach this new location
                visited.add(e)
                to_visit.put(e)
                children[vertex].append(e)
    return (visited,paths)

# found this on internet
def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

# found this on internet
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

# list(bfs_paths(graph, 'A', 'F')) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
