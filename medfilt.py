from dataclasses import replace
import numpy as np
import scipy
from scipy.signal import medfilt
from collections import Iterable

window_filter = 5 #Filter's window
input_file = "input.bin"
output_file = "output.bin"
#convert a nested list into a one-dimensional list
def flatten(list): 
     for item in list:
         if isinstance(item, Iterable) and not isinstance(item, str):
             for x in flatten(item):
                 yield x
         else:        
             yield item

content = []
with open(input_file) as f:
    # read first line and add elements if these elements is number
    h = [int(x) for x in next(f).split() if x.isdigit()] 
    content.append(h)

    # read rest of lines
    for line in f: 
        content.append([int(x) for x in line.split() if x.isdigit()])

output = open(output_file, "w")
#convert to 1D array
Dimension_1D = list(flatten(content)) 
#Median filter
outFilter = scipy.signal.medfilt(np.array(Dimension_1D), window_filter) 

#Delete characters, which are not number
data_out= str(outFilter).replace("[", "") 
data_out = data_out.replace("]", "")

output.write(data_out)

print(type(Dimension_1D))
print(Dimension_1D)

print(outFilter)
