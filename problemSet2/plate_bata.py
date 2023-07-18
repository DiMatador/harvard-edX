def is_valid(s):
    """str > bool
    Returns True if the plate is valid, False otherwise.
    AAA222 would be an acceptable vanity plate.
    AAA22A would not be acceptable.
    The first number used cannot be '0'.
    """
    if len(s) < 2 or len(s) > 6:
        return False
    elif not s[0].isalpha() or s[0] == '0':
        return False
    elif any(char in [",", ".", "-", "_", "/"] for char in s):
        return False

    for i in range(1, len(s) - 1):
        if s[i].isdigit():
            return False

    return True


is_valid('CS50P2')