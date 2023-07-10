""" working file bata """

import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    """str -> int
    Returns the number of times 'num' appears in a text
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
    r"(\bum)"
    """
    words = list()

    """ scan the file for the word 'um' using RE """
    if um := re.finditer(r"(\b[uUmM][^!?]\b)", s, re.IGNORECASE):
        if um:
            for word in um:
                found_um = word.group()
                words.append(found_um.lower())

    """ count the number of time the 'um' appears """
    return words.count("um")


if __name__ == "__main__":
    main()
