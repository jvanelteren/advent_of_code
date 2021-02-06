# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
f=open('input.txt')
lines = [line.rstrip('\n') for line in f]

allingredients = []
allergens = {}

for line in lines:
    ing, all = line.split(' (contains ')

    all = all[:-1].split(', ')
    ing = ing.split()
    allingredients += ing
    for a in all:
        if a not in allergens:
            allergens[a] = set(ing)
        else:
            allergens[a] &= set(ing)

allallar = {i for v in allergens.values() for i in v}

ans = 0
for i in allingredients:
    if i not in allallar:
        ans+=1
print(ans)

# %%
# part 2
allergens = {a : list(ing) for a, ing in allergens.items()}
while any(True for ing in allergens.values() if isinstance(ing, list) and len(ing) > 1):
    for a, ing in allergens.items():
        if isinstance(ing, list) and len(ing) == 1: # found one
            allergens[a] = ing[0]
            for a2, ing2 in allergens.items(): # remove the item from other lists
                if isinstance(ing2, list) and ing[0] in ing2:
                    ing2.remove(ing[0])


ans = list(allergens.keys())
ans.sort()
print(','.join([allergens[i] for i in ans]))
# %%
