
# implement a fuel indicating script
# main function:
def main():
    fuel_gauge()

# logical function:
def fuel_gauge():
    x,y = 0,0
    try:
        fuel = input("Fraction: ")
    except ValueError:
        pass

        for ch in fuel:
            separator = ch.split('/')

            x = int(ch[0])
            y = int(ch[1])
            average = (x/y) * 100
            return average

# call main
main()
