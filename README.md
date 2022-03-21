# **Command line utility for linux to analysis median filter**  
First of all, you need to install `python3`      
Used libraries  
```
numpy: $ pip install numpy
scipy: $ sudo apt-get install python3-scipy
typer: $ pip install typer 
```   
For more information, see "[typer](https://github.com/tiangolo/typer)" and "[scipy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.medfilt.html)" 

Create input file(data to filter) in **_current working directory_**:  
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
```  
Note:  
``` 
1. Filter's window: Integer  
2. Input file name (Name of input file): string  
3. flag (This is optional field):  
--f/--no-f: Create output.bin file in **current working directory** to save output data from filter
```  

See more details:  
``` 
$ ./medfilt.py --help  
```    

