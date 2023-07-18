def main():
    plate = input("Plate: ").upper()

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    """str > str
    Returns a boolean if the plates is True or False
    AAA222 would be an acceptable … vanity plate
    AAA22A would not be acceptable.
    The first number used cannot be a ‘0’.
    """
    punctuation = [",", ".", "-", "_", "/"]
    for letter in s:
        if letter in punctuation:
            return False
        elif s[2:3].isdigit() and s[2:3] == '0':
            # print(s[2:3]) cheek the third digit not zero
            return False
        elif s[3:5].isalpha():
            return True

    ct = 0
    while ct < 7:
        for _ in s:
            if not s[:1].isalpha() or len(s) < 2 or len(s) > 6:
                return False
            else:
                return True
        ct += 1


main()
