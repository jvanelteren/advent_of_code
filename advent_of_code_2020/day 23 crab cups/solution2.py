#%%
code = "916438275"

class Node():
    def __init__(self, num):
        self.num = num
        self.left = None
        self.right = None

    def __repr__(self):
        return f'value {self.num} left {self.left.num if self.left else ""} right {self.right.num if self.right else ""}\n'

nodes = [Node(int(n)) for n in code]
nodes.extend([Node(i) for i in range(10, 1000001)])

for l,n,r in zip(nodes, nodes[1:], nodes[2:]):
    n.left = l
    n.right = r
nodes[0].left = nodes[-1]
nodes[0].right = nodes[1]
nodes[-1].left = nodes[-2]
nodes[-1].right = nodes[0]

#%%
H = {n.num: n for n in nodes}
MINIM = 1
MAXIM = 1000000

cur_node = H[int(code[0])]

for i in range(10000000):
    if i % 1000000 == 0 : print(i)

    pickup = [cur_node.right, cur_node.right.right, cur_node.right.right.right]
    cur_node.right = pickup[-1].right
    pickup[-1].right.left = cur_node
    pickup_nums = {n.num for n in pickup}

    search_num = cur_node.num - 1
    if search_num < MINIM:
        search_num = MAXIM

    while search_num in pickup_nums:
        search_num -= 1
        if search_num < MINIM:
            search_num = MAXIM
    search_node = H[search_num]

    search_node.right.left = pickup[-1]
    pickup[-1].right = search_node.right
    search_node.right = pickup[0]
    pickup[0].left = search_node
    cur_node = cur_node.right

H[1].right.num * H[1].right.right.num

# %%
