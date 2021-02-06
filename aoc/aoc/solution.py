# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
from collections import Counter, defaultdict, namedtuple, deque
from math import gcd, ceil
import re
import networkx as nx
from dataclasses import dataclass
import itertools
import aoc
from matplotlib import pyplot as plt
import string
# plt.imshow(pic)


# %%
f=open('input.txt')
lines = [line.rstrip('\n') for line in f]
line = lines[0]
line


# %%