""" working file """

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    """example return str:
    https://youtu.be/xvFZjo5PgG0
    """
    """ re.IGNORECASE matches A == a upper and lower, case incensitive
    Note: (?:something) this means do not capture this group
    """
    # pattern = "(h[http]*s?)(\:\/\/w{0,3}\.?y[out]*u)(be)(\.com\/e[mbe]*d)(\/\w*Pg[G]*0)"
    pattern = r"(https?://)(?:www\.)?(youtu)(be)(\.com/embed)(/[a-zA-Z0-9]*)"
    result = re.search(pattern, s, re.IGNORECASE)
    if result == None:
        return None

    p1, p2, p3, p5 = result.group(1), result.group(2), result.group(3), result.group(5)
    """ if the length of 'p1' is 4 and missing the 's' sub the s in """
    # must add the s to http, == https
    p3 = re.sub(r"(b)", r".\1", str(p3))
    
    if 's' not in p1:
        p1 = re.sub(r"(http)", r"https\1", str(p1))

    lst = list()
    for n in (p1, p2, p3, p5):
        lst.append(n)
        result = "".join(lst)

    return result


if __name__ == "__main__":
    main()

# start
^\<i\w+e

# end
\<\/i\w+\>$