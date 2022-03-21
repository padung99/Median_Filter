import numpy as np
import scipy
from scipy.signal import medfilt
from collections import Iterable

window_filter = 5 

def flatten(lis): #convert a nested list into a one-dimensional lis
     for item in lis:
         if isinstance(item, Iterable) and not isinstance(item, str):
             for x in flatten(item):
                 yield x
         else:        
             yield item

content = []
with open('input.bin') as f:
    h = [int(x) for x in next(f).split() if x.isdigit()] # read first line
    content.append(h)
    for line in f: # read rest of lines
        content.append([int(x) for x in line.split() if x.isdigit()])


Dimension_1D = list(flatten(content))
outFilter = scipy.signal.medfilt(np.array(Dimension_1D), window_filter)

print(type(Dimension_1D))
print(Dimension_1D)

print(outFilter)
