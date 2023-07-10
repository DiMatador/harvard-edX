import re
import sys

"""
    Checks if the given IP address is valid or non-numeric characters.
    Returns True if the IP address is valid, False otherwise.
"""
 
def main():
    print(validate(input("IPv4 Address: ")))
    
    
def validate(ip):
    # searching pattern
    pattern = re.search(r'^\d+\.\d+\.\d+\.\d+$', ip)
    
    # check for None numeric
    if pattern is None:
        return False
    # group and split the numbers
    result = pattern.group().rsplit('.')
     
    # check if the numbers are within range 0 to 255
    for  num in result:
        if int(num) not in range(0, 255):
            return False
        
    # check the length of the ip address
    if len(result) != 4:
        return False
        
    return True
    
if __name__ == "__main__":
    main()