''' Assignment 1  from problem set 6  Lines of code '''
import sys
from sys import argv

line_ct = list()
ct = 0
cm = 0
#program that expects exactly one command-line argument '''
try:
    scrip, file = argv
    #exit if not a python file
    if file.endswith('.py') == False:
        sys.exit("Not a python file")
except ValueError:
    #less than 2 command-line arguments
    if len(argv) < 2:
        sys.exit("Too few command-line arguments")
   
    #more than 2  command-line arguments
    if len(argv) > 2:
        sys.exit("Too many command-line arguments") 
        
    else:
        pass
# this is a comment should count included in the count       
try:
    with open(file) as infile:              
        #count the lines of code
        for lines in infile:
            if lines.strip() and "#" not in lines:
                if "# " in lines:
                    pass
                ct+=1
        #check on comments

except FileNotFoundError:
    #File does not exist
    sys.exit("File does not exist")
else:
    print(ct)