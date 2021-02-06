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
# at beginning look at example first and highlighted texts

# %%

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
                    seen.add(n)
                    frontier.append(n)
                    # paths[n] = paths[search]+[n]
                    parents[n]= search
                    if goal and n == goal:
                        # print('goal found')
                        return parents
                        # return paths[goal],parents
        seen.add(search)
    if goal: return False
    else: return parents

# %%
def open(x,y):
    if y>=0 and x>=0:
        n = bin((x*x + 3*x + 2*x*y + y + y*y) +1358).count('1')
        if n%2==0: 
            return True
        else: return False

def getneigh(inp):
    x,y = inp[0],inp[1]
    res = []
    if open(x+1,y): res.append((x+1,y))
    if open(x-1,y): res.append((x-1,y))
    if open(x,y+1): res.append((x,y+1))
    if open(x,y-1): res.append((x,y-1))
    return res
par = (bfs(getneigh,(1,1),(31,39)))

# %%
def get_path(parents,goal):
    # print(start,goals)
    cur = goal
    path = [cur]
    while cur != (1,1):
        cur = parents[cur]
        path.append(cur)
    path.reverse()
    return path

print(len(get_path(par,(31,39)))-1)
print(len([p for p in par if len(get_path(par,p))-1<=50]))


# %%

# %%
