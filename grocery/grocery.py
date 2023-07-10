# create a script to intake items for a list
# imports

#main function
def main():
    grocery_lst = grocery_list('')
    return(grocery_lst)

# logical function ======================================================================
def grocery_list(order):
    ''' function to keep track of items, returns items in order with all letters capitalized '''
    input_lst = []
    counted = dict()
    
    while True:

        try:
            grocery_lst = input(order)
            input_lst.append(grocery_lst)
            input_lst = sorted(input_lst)
        except(EOFError):
            '''count the times an item was entered '''
            for ct in input_lst:
                if ct in counted:
                    counted[ct] = counted[ct] + 1
                else:
                    counted[ct] = 1
            ''' Loop through the dict to print the resulting list of items '''
            for key, value in counted.items():
                print(value, key.upper())

            break # if ctr-D entered exit

        continue # while True continue

# call main
main()