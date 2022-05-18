import sys #importing sys modules
script, input_encoding, error = sys.argv #taking in input_encoding and error from command args

def main(language_file, encoding, errors): #defining main function which takes these args
    line = language_file.readline()  #reads one line
    if line: #unless line doesn't exist (we are at the end of the file)
        print_line(line, encoding, errors) #use the print line function 
        return main(language_file, encoding, errors) #
    
def print_line(line, encoding, errors): #defines print line function
    next_lang = line.strip() #
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding= "utf-8")


main(languages, input_encoding, error)
