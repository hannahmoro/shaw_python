from sys import argv #import the argv module from sys
from os.path import exists #import the exists module from os.path

script, from_file, to_file = argv #takes in from_file and to_file variables as arguments

print(f"Copying from {from_file} to {to_file}") #message

#we could do these two on one line, how
in_file = open(from_file) #opens from file and saves it as in_file
indata = in_file.read() #reads in_file and saves contents as indata

print(f"The input file is {len(indata)} bytes long") #message that shows n bytes in the from_file

print(f"Does the output file exist? {exists(to_file)}") #message that shows whether the to_file exists
print("Ready, hit RETURN to continue, CTRL-C to abort.") #message
input() #takes input of RETURN vs CTRL-C

out_file = open(to_file, 'w') #opens to_file with write permissions
out_file.write(indata) #writes indata to the to_file

print("Alright, all done.") #message

out_file.close() #closing up
in_file.close()



