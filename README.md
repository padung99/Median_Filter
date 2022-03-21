First of all, you need to install `python3`    
Used libraries  
```
numpy: $ pip install numpy
scipy: $ sudo apt-get install python3-scipy
typer: $ pip install typer 
```    
Create input file(data to filter) in working directory:  
```
$ touch input.bin
```    
Set permission to run script:  
```
$ chmod +x medfilt.py
```    
Run script to receive output data from filter:  
```  
$ ./medfilt <Filter's window> <Input file name> <flag>
Filter's window: Integer  
Input file name (Name of input file): string  
flag (This is optional field):  
--f/--no-f: Create output.bin file in current working directory to save output data from filter
```    
See more details:  
``` 
$ ./medfilt.py --help  
``` 
