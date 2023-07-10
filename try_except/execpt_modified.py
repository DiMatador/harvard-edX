# shorter version of the try/except

# main
def main():
    ''' use main to invoke get_int function '''
    x = get_int("What's the value of X? ")
    print(f"Value of X {x}")

# logical function
def get_int(prompt):
    ''' function to check if an input is an integer '''
    while True:
        try: # we can get rid of the extra variable, also return  right from here
            return int(input(prompt))
        except ValueError:
# here we could use the "pass" function to just keep on asking the user for and integer instead of the 'x is not an integer message'
            pass # this is used by choice
            # print("X: Not an integer")
# call number
main()
