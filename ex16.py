from sys import argv #import the argv module

script, filename = argv #grab a filename variable from the terminal when running the script

print(f"We're going to erase {filename}.") #message
print("If you don't want that, hit CTRL-C (^C).") #message
print("If you do not want that, hit RETURN.") #message

input("?") #will provide a prompt to hit either CTRL-C or RETURN

print("Opening the file...") # (if RETURN) message
target = open(filename, 'w') #opens a file with write permission and names that opened file target

print("truncating the file. Goodbye!") #message
target.truncate() #deleted the file named target

print("Now I'm going to ask you for three lines.") #asks for entry and saves as vars line1:line3
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.") #message


#simplifying
target.write(f"{line1} \n {line2} \n {line3} \n")

# target.write(line1) #write each line, separated into lines by \n
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print("And finally, we close it.") #message
target.close() #close the file named target