# classes first lecture on it

import sys

def main():
    hello("World")
    goodbye("World")
    
def hello(name):
    print(F"Hello, {name}")
    
def goodbye(name):
    print(F"Hello, {name}")
    
    

''' play close attention, main gets called and it will execute all that main
is calling (hello() and goodbye()).
when importing a file or library we need to dismiss main so we can call
only what we need from the library(file) in this case only hello is been called
by say'''
# call main (normal way to call if we want to execute this file)
# main()

''' now lets use this file as a library, to do so we need to call main()
in this mannor '''

if __name__ == "__main__":
    main