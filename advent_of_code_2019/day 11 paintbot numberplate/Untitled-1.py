# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython


# %%
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'day 11'))
	print(os.getcwd())
except:
	pass


# %%
from computerrefractored import Computer
import copy

# %%
noun, verb = 0,0
f=open('input.txt').read()
memory = tuple(int(i) for i in f.split(',')) # let's make it immutable as a tuple
memsize = 100000
memory = tuple(list(memory)+[0]*memsize)
c = Computer(list(memory),noun,verb,[1])

from collections import defaultdict
class Grid():
    def __init__(self):
        self.x,self.y = 0,0
        self.visited = defaultdict(int)
        self.color = defaultdict(int)
        self.orientation = {
            'up':(0,1),
            'left':(-1,0),
            'down':(0,-1),
            'right':(1,0)
        }
        self.cur_orient = 'up'
    def paint(self,color_to_paint):
        self.color[(self.x,self.y)]=color_to_paint
    
    def get_color(self):
        return self.color[(self.x,self.y)]
    def get_location(self):
        return (self.x,self.y)
    def move(self):
        dx,dy = self.orientation[self.cur_orient]
        self.x += dx
        self.y += dy
        self.visited[(self.x,self.y)]=1 
    
    def turn(self,turn):
        print('ins',turn)
        if turn == 0:
            if self.cur_orient=='up':self.cur_orient='left'
            if self.cur_orient=='down':self.cur_orient='right'
            if self.cur_orient=='left':self.cur_orient='down'
            if self.cur_orient=='right':self.cur_orient='up'
        print('ins',turn)
        if turn == 1:
            if self.cur_orient=='up':self.cur_orient='right'
            if self.cur_orient=='down':self.cur_orient='left'
            if self.cur_orient=='left':self.cur_orient='up'
            if self.cur_orient=='right':self.cur_orient='down'
        print('ins',turn)


# %%

grid = Grid()
def walk():
  current_color = grid.get_color()
  c.receiveinput(current_color)
  color_to_paint = c.run()
  turn = c.run()
  print('turn',turn)
  grid.paint(color_to_paint)
  print('cur',grid.cur_orient)
  grid.turn(turn)
  print('cur',grid.cur_orient)
  grid.move()
  print(f'cur location{grid.get_location()},current_color{current_color},color_to_paint{color_to_paint},turn{turn},{grid.cur_orient}')

def traverse():
  cur = 1
  while cur !=(0,0) and c.running:
      walk()
      cur = grid.get_location()


# %%
traverse()


# %%


