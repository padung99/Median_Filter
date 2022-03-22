#!/usr/bin/env python3

#This script is written by Phan Anh Dung (Фан Ань Зунг)
#More details in README.md
#github: https://github.com/padung99/Median_Filter

import numpy as np
import scipy
from scipy.signal import medfilt
import collections
import typer 

try:
    collectionsAbc = collections.abc
except AttributeError:
    collectionsAbc = collections

try:
    from collections.abc import Iterable 
except ImportError:
    from collections import Iterable 

app = typer.Typer()

output_file = "output.bin"

#convert a nested list into a one-dimensional list
def flatten(list): 
     for item in list:
         if isinstance(item, Iterable) and not isinstance(item, str):
             for x in flatten(item):
                 yield x
         else:        
             yield item

@app.command()
def filter(w: int = typer.Argument(..., help="[int] Window's median filter"),
           ifile: str = typer.Argument(..., help="[File's name] Input data to median filter (From .bin file)"),
           f: bool = typer.Option(False, help='[File] Create output.bin in this working directory to save output data from median filter')):
    window_filter = w
    
    input_file = ifile

    content = []
    with open(input_file) as file:
        # read first line and add elements if these elements are number
        h = [int(x) for x in next(file).split() if x.isdigit()] 
        content.append(h)

        # read rest of lines
        for line in file: 
            content.append([int(x) for x in line.split() if x.isdigit()])

    #convert to 1D array
    Dimension_1D = list(flatten(content))

    #Median filter
    outFilter = scipy.signal.medfilt(np.array(Dimension_1D), window_filter) 

    #Delete characters, which are not number
    data_out= str(outFilter).replace("[", "") 

    #output array to file ###########
    data_out = data_out.replace("]", "")
    
    if f:
        #write data to ouput file
        output = open(output_file, "w")
        output.write(data_out)

    #stdout
    typer.echo(f"Output data:  {data_out}")
    

if __name__ == "__main__":
    app()
