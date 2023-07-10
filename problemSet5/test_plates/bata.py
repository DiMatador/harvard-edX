import sys

def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
        sys.exit(0)  # valid plate, exit with code 0
    else:
        print("Invalid
        ")
        sys.exit(1)  # invalid plate, exit with code 1

def is_valid(s):
    # your validation logic here
    # return True if valid, False if invalid
    # e.g.
    if len(s) != 6:
        return False
    elif not s[:2].isalpha():
        return False
    elif not s[2:].isdigit():
        return False
    elif s[2] == '0':
        return False
    else:
        return True

if __name__ == "__main__":
    main()
