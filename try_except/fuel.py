# script to calculate the fuel in a car

# main function
def main():
    try:
        fuel = gauge(input("Fraction: "))
    except ValueError:
        pass
    else:
        print(fuel)



#============================================================
# logical function

def gauge(m):
    banana = m.split('/')
    return banana
    
    




# invoke main
main()