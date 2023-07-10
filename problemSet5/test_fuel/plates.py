""" write a module that takes 6 characters
1. must start with two letters, first two characters can not be numbers
2. minimum two characters
3. first digit is not a zero
4. numbers can not be in the middle eg: AAAA22 its good, AAA22A not acceptable
5. No puntuations
"""

def main():
    plate = input("Plate: ").upper()
    validate = is_valid(plate)
    print(validate)
    
    
def is_valid(s):
    ct = 0
    while ct < 7:
        for _ in s:
            if s[0].isalpha() and s[1].isalpha() and len(s) >= 2 and len(s) <= 6:
                # check for a zero as first characters
                for zero in s:
                    if zero.isdigit():
                        # save the location of zero
                        fd = s.index(zero)
                        if s[fd].isdigit() and zero != '0':
                            return F"Valid"
                        else:
                            return F"Invalid"
                return F"Valid"
            else:
                return F"Invalid"
        ct+=1
        
        break
        
    
if __name__ == "__main__":
    main()