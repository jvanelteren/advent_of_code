from collections import namedtuple

def dimensions(obj): #gets an iterable of tuples and returns the minimums and maximums and ranges
    minim = [min(obj,key = lambda x:x[i])[i] for i in range(len(obj[0]))]
    maxim = [max(obj,key = lambda x:x[i])[i] for i in range(len(obj[0]))]# max for dimensions
    ranges = [maxim[i] - minim[i]+1  for i in range(len(obj[0]))]
    Dim = namedtuple('Dim',['min','max','ranges'])
    res = Dim(minim,maxim,ranges)
    return res

def normalize(obj): #takes a list of coordinates and returns it normalized (getting rid of negatives)
    dim = dimensions(obj)
    return [[o[i]-dim.min[i] for i in range(len(obj[0]))] for o in obj]
def manhattan(x,y):
    return abs(x[0]-y[0])+abs(x[1]-y[1])