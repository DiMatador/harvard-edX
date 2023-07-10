import sys

# importing just one of the functions for now
from sayings import hello

''' note that calling the hello from the sayings import 
will also call all that is in the sayings file '''

if len(sys.argv) == 2:
    hello(sys.argv[1])# call only the hello() here see what happens
    
   