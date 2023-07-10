import re


def main():
    print(count(input("Text: ")))


def count(s):
    """str -> int
    Returns the number of times 'um' appears in a text
    >>> count('hello, um, world')
    1
    >>> count('um, hello, um, world')
    2
    >>> count('um...')
    1
    >>> count('yum')
    0

    Notes:
    case-insensitively, as a word unto itself
    case-insensitively, not as a substring of some other word
    Test RE codes
    r"(\bum)"
    (\b[uUmM][^!?]\b)
    """
    return sum(1 for _ in re.finditer(r"(\b[uUmM][^!?]\b)", s, re.IGNORECASE))


if __name__ == "__main__":
    main()
