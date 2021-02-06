#%%
# always check the input carefully after opening and splitting
# split r and c indices for simplicity (instead of combining them into a tuple)
# when using re, be sure to thing if greedy or nongreedy parsing is necessary
# don't use re when split() suffices, whitespaces can be casted to int
# make sure to experiment with one item from a list instead of and immediate for loop
# !when there is a clear test case available, test it!
# scan over the input a bit more carefully, it may be different than the test examples
# when plotting, use plt.imshow (not plt.show)
# i should pad_dir into itertools more
# when refractoring a test case into the real code, check the indices are not hardcoded!
# use better descriptive names. also unpack if it makes code more readable for example in list of tuples
# with regex you can numbers pretty easily in a line. and -? to add possible negatives
# sometimes its easier to brute force bfs than to figure out an insane algo yourself
# at beginning pad_dir at example first and highlighted texts
# utils for bfs make you really fast! boom place 13 on leaderboard
# try to bruteforce if not clear if you have to take a smart shortcut
# when checking if string appears in list of strings, be careful to use ' '.join not ''.join
# pay attention to parentheses when coding an condition, e.g. with mod
# pay attention to the types that you're using: [2929] != ['2929'] != list('2929') != [2,9,2,9]
# don't put things in a list and then to tuple when () is enough
# experiment with %debug instead of print statements
# while doing the puzzle, just make it work instead of dreaming about fancy stuff that you don't know about yet



# %%
def neighbors1d(arr,conv_shape,mode='same',padding=None,pad_dir='center') ->list:
    """
    Returns a list of kernel views of a string or list 
    mode == 'valid': returns only results where the kernel fits
    mode == 'same': return the same amount of items as original
    when mode =='same', default padding is the outer value
    """
    if padding:
        to_pad = padding # user specified padding
    else:
        to_pad = arr[0] # begin or end of list
    
    if isinstance(arr,list): # to convert a list temporarily to string
        arr_is_list = True
    else:
        arr_is_list = False

    if mode == 'valid':
        pass

    p_size = conv_shape//2
    if mode == 'same':
        if arr_is_list:
            arr = ''.join(arr)
        if isinstance(arr,str): #here the padding is applied
            if pad_dir == 'center':
                arr = to_pad*p_size+arr+to_pad*p_size
            if pad_dir == 'left':
                arr = to_pad*(conv_shape-1)+arr
            if pad_dir == 'right':
                arr = arr+to_pad*(conv_shape-1)
        else:
            return 'only string and list supported'
        if arr_is_list:
            arr = list(arr)

    if conv_shape % 2 == 1: # odd conv_shape
        return [arr[i-p_size:i+p_size+1] for i in range(p_size,len(arr)-p_size)]
    else: # even conv_shape
        return [arr[i:i+conv_shape] for i in range(0,len(arr)-conv_shape+1)]

inp = open('input.txt','r').read()
traps = ['^^.','.^^','^..','..^']
def getnext(inp):
    res = ['^' if conv in traps else '.' for conv in neighbors1d(inp,3,padding='.')]
    return ''.join(res)

iterations = 40
# iterations = 400000
res = [inp]
for i in range(iterations-1):
    inp = getnext(inp)
    res.append(inp)
sum([r.count('.') for r in res])