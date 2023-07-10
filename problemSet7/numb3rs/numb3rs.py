import re
import sys

def main():
    print(validate(input("IPV4 Address: ")))

def validate(ip):
    numbers = list()
    # read pattern
    pattern = re.search(r'\d.+\d', ip)
    # group and split all extracted number
    address = pattern.group().rsplit('.')
    # add the numbers to a list, check that the list of length 4 not more or less
    for num in address:
        numbers.append(int(num))
        
    # check if the numbers are within range 0 to 255
    for nums in numbers:
        if nums not in range(0, 255):
            return False
        # check the length of the ip address
        elif len(address) > 4 or len(address) < 4:
            return False
        else:
            return False
    return True
if __name__ == "__main__":
    main()