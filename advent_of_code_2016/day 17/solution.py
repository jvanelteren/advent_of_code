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
# utils for bfs make you really fast! boom place 13 on leaderboard
# try to bruteforce if not clear if you have to take a smart shortcut
# when checking if string appears in list of strings, be careful to use ' '.join not ''.join
# pay attention to parentheses when coding an condition, e.g. with mod
# pay attention to the types that you're using: [2929] != ['2929'] != list('2929') != [2,9,2,9]
# don't put things in a list and then to tuple when () is enough

import hashlib
from collections import deque

code = 'vkjiggvb'

def getpos(path):
    dr = path.count('D')-path.count('U')
    dc = path.count('R')-path.count('L')
    if -1 < dr < 4 and -1 <dc <4:
        return (dr+1,dc+1)
    else: return False

def getneigh(state):
    path,pos = state[0],state[1]
    res = []
    h = hashlib.md5((code+path).encode('utf-8')).hexdigest()
    if h[0] in list('bcdef') and getpos(path + 'U'):res.append((path+'U',getpos(path+'U')))
    if h[1] in list('bcdef') and getpos(path + 'D'):res.append((path+'D',getpos(path+'D')))
    if h[2] in list('bcdef') and getpos(path + 'L'):res.append((path+'L',getpos(path+'L')))
    if h[3] in list('bcdef') and getpos(path + 'R'):res.append((path+'R',getpos(path+'R')))
    return res

def bfs(connections, start, goal=None):
    seen = set() # the locations that have been explored
    frontier = deque([start]) # the locations that still need to be visited
    parents = {start: None}
    while frontier:
        search = frontier.popleft()
        neighbors = connections(search)
        if neighbors:
            for n in neighbors:
                if n not in seen:
                    seen.add(n)
                    if n[1]!=(4,4):
                        frontier.append(n)
                    parents[n]= search
        seen.add(search)
    if goal: return False
    else: return parents
res = bfs(getneigh,('', (1, 1)))
res = ([(len(r[0]),r[0]) for r in res if r[1]==(4,4)])

# part 1 and 2
min(res)[1],max(res)[0]
