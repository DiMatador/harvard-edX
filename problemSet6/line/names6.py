# Reads from a file, one line at a time
# print the list sorted

with open("names.txt") as file:
    """ this is a doc string not ignore
    its a multi line doc string
    """
    for line in sorted(file):
        
        print("hello,", line.rstrip())
        
    ''' test test doctstring '''
# test test comment line