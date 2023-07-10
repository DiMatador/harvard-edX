# script to convert a string to a snake case variable name
# main function
def main():
    phrase = snakie(input("Camel case: "))
    print(phrase)


#=========================================================================================
# function to conver to snake case
def snakie(m):
    phrase = m
    on_split = ""
    for l in phrase:
        if(l.isupper()):
            on_split+= "^" + l
            on_split = on_split.lower()
            # print(on_split)
        else:
            on_split += l
            # print(on_split)
    on_split = on_split.split("^")

    for j in on_split:
        print(j+'_', end='')
        #return j

# call main
main()
