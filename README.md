# **Command line utility for linux to analysis median filter**  
First of all, you need to install `python3`      
Used libraries  
```
numpy: $ pip install numpy
scipy: $ sudo apt-get install python3-scipy
typer: $ pip install typer 
```   
For more information, see "[typer](https://github.com/tiangolo/typer)" and "[scipy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.medfilt.html)" 

Create input.bin file(data to filter) in **_current working directory_**:  
```
$ touch input.bin
```    
Set permission to run script:  
```
$ chmod +x medfilt.py
```    
Run script to receive output data from filter:  
```  
$ ./medfilt.py <Filter's window> <Input file name> <flag>
```  
Note:  
``` 
1. Window's filter: Integer  
2. Input file name (Name of input file): string  
3. flag (This is optional field):  
--f/--no-f: Create output.bin file in **current working directory** to save output data from filter
```  

See more details:  
``` 
$ ./medfilt.py --help  
```    
### **Examples:**  
Input data from "**input.bin**":  
``` 
4 5 6 9 16 04 99 25 36 99 14 25 12 36 97 14 74 56 23 36 114 14
```  
1. **Command**(stdin) **without flag** --f:  
``` 
$ ./medfilt.py 5 input.bin  
```   
**Output**(stdout) on **console**:  
``` 
Output data:   4  5  6  6  9 16 25 36 36 25 25 25 25 25 36 56 56 36 56 36 23 14
```  
2. **Command**(stdin) **with flag** --f:  
```
$ ./medfilt.py 5 input.bin --f  
```   
**Output**(stdout) on **console**:  
``` 
Output data:   4  5  6  6  9 16 25 36 36 25 25 25 25 25 36 56 56 36 56 36 23 14
```  
**Output** to "**output.bin**":  
```
 4  5  6  6  9 16 25 36 36 25 25 25 25 25 36 56 56 36 56 36 23 14
```
