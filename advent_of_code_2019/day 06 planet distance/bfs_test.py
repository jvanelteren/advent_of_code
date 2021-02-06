# %%
from collections import deque


def get_orbit_map():
    # not with read because thats probably the whole file
    f = open('input.txt')
    lines = [line.rstrip('\n').split(')') for line in f]
    return {l[1]: [l[0]] for l in lines}


o = get_orbit_map()
print(len(o))
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
    parents = {start: None}

    def get_path(parents):
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
                    frontier.append(n)
                    # paths[n] = paths[search]+[n]
                    parents[n]= search
                    if goal and n == goal:
                        # print('goal found')
                        return get_path(parents)
                        # return paths[goal],parents
        seen.add(search)
    if goal: return False
    else: return parents

def geto(k):
    return o.get(k,None)
len(bfs(geto,start='YOU',goal='COM'))
# %%
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
    if goal in parents: return get_path(parents)
    else: return False

conn = {'A':[('B',1),('C',7),('D',5)],
        'B':[('C',6)],
        'C':[('D',1)],
        'D':[('C',1)],

}
dijkstra(conn,start='A',goal='C')


# %%
