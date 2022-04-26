from sys import argv #import the argv module

script, filename = argv #use argv to get the filename (from the terminal command)

txt = open(filename) #save the file text as txt

print(f"Here's your file {filename}:") #prints a message with the name of the file
print(txt.read()) #reads the txt file with no parameters and prints

print("Type the filename again:") #another message
file_again = input("> ") #this time gets the file name from prompt and not from txt

txt_again = open(file_again) #this time opens the new file name arg

print(txt_again.read()) #reads the txt file from the new variable and prints that

txt.close()
txt_again.close()
