""" write a module that takes 6 characters
1. must start with two letters, first two characters can not be numbers
2. minimum two characters
3. first digit is not a zero
4. numbers can not be in the middle eg: AAAA22 its good, AAA22A not acceptable
5. No puntuations
"""

import sys

def main():
    plate = input("Plate: ").upper()

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    for _ in s:
        if s[0].isalpha() and s[1].isalpha() and len(s) >= 2 and len(s) <= 6:
            """ loop through s and check for zero as first digit,
                check for none alphanumeric characters
            """
            for zero in s:
                if not s.isalnum():
                    return False
                if zero.isdigit():
                    # save the location of zero
                    fd = s.index(zero)
                    if s[fd].isdigit() and zero != '0':
                        return True
                    else:
                        return False
            return True
        else:
            return False

if __name__ == "__main__":
    main()