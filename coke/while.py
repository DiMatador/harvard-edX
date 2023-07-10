#==============================================================
print("======================While loops=======================\n")

#main function
def main ():
	number = get_number()
	meow(number)
	
	
# get number from user
def get_number():
    
    #use a while loop to continually get a number
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break;
    return n
    
    
# number of time to meow
def meow(n):
    for _ in range(n):
        print("meow")
        
main()