from sys import argv

script, filename = argv 

new_file = open(filename)

print(new_file.read())