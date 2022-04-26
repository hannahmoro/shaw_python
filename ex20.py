from sys import argv #import the argv module from sys

script, input_file = argv #sets input_file from terminal argument

def print_all(f): #function that reads the file f
    print(f.read())

def rewind(f): #function that moves focus to first line of the file f
    f.seek(0)

def print_a_line(line_count, f): #function that prints the specified line number from file f
    print(line_count, f.readline())

current_file = open(input_file) #opens the file specified in terminal argument

print("First let's print the whole file:\n")

print_all(current_file) #uses our print_all function to print the entire file

print("Now let's rewind, kind of like a tape.")

rewind(current_file) #uses our rewind function to move to the begining of the file

print("Let's print three lines:")

current_line = 1 #sets var
print_a_line(current_line, current_file) #prints line [current_line] from the file

current_line = current_line + 1 #increments up by one
print_a_line(current_line, current_file) #prints the new [current_line} from the file]

current_line = current_line + 1 #same deal
print_a_line(current_line, current_file)

