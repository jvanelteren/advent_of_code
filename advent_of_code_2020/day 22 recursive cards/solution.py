# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from collections import deque
from itertools import islice

f = open('input.txt').read().split('\n\n')
players = []
for p in f:
    _, *vals = p.split('\n')
    players.append(deque(int(v) for v in vals))
p1, p2 = players


# %%
# this is the puzzle of many small mistakes. In the end nothing to bad
# small mistake: couldnt figure out how to parse
# well done: take losses and go with two input files initially
# well done: recogizing this is a nice use case for deque
# mistake: did not multiply by 1,2,3 but by 0,1,2 etc
# mistake: played new game with copys of deck instead of length of deck
# mistake: did forget about the rule to stop when same cards where dealt
# mistake: did check for same cards to stop game instead of same hand

def play_crabs(p1,p2, recurse = False, first= False):
    round = 0
    played = set()
    while(p2 and p1):
        round+=1

        if recurse and ((tuple(p1),tuple(p2)) in played):
            break
        else:
            played.add((tuple(p1),tuple(p2)))
        c1, c2 = p1.popleft(), p2.popleft()


        if recurse and len(p1) >= c1 and len(p2) >= c2:
            p1new = deque(islice(p1, 0, c1))
            p2new = deque(islice(p2, 0, c2))
            winner, _ = play_crabs(p1new, p2new, recurse)
            if winner == 1:
                p1.extend([c1,c2])
            if winner == 2:
                p2.extend([c2,c1])

        else: # compare cards
            if c2 > c1:
                p2.extend([c2,c1])
            else:
                p1.extend([c1,c2])

    if p1 and p2: # same situation: p1 won
        return (1, p1)
    elif p2:
        return(2, p2)
    elif p1:
        return (1, p1)

# part 1
_ , ans = play_crabs(p1.copy(),p2.copy(), recurse=False)
print(sum((i+1)*c for i, c in enumerate(list(reversed(ans)))))

# part 2
_ , ans = play_crabs(p1,p2, recurse=True, first = True)
print(sum((i+1)*c for i, c in enumerate(list(reversed(ans)))))


# %%
