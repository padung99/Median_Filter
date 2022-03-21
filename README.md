Create input file(data to filter) in working directory:__
$ touch input.bin

Set permission to run script:__
$ chmod +x medfilt.py

run script to receive output data from filter:__
$ ./medfilt <Filter's window> <Input file name> <flag>

Filter's window: Integer__
Input file name (Name of input file): string__
flag (This is optional field):__
--f/--no-f: Create output.bin file in current working directory to save output data from filter
  
See more details:__
$ ./medfilt.py --help__
 
