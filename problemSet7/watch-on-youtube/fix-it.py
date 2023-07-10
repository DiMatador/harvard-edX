import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    """
    (str) -> str
    Returns a shorter version of a Youtube like.
    parse(https://www.youtube.com/embed/xvFZjo5PgG0)
    >>> https://youtu.be/xvFZjo5PgG0
    parse(https://youtube.com/embed/xvFZjo5PgG0)
    >>> https://youtu.be/xvFZjo5PgG0

    Note:
    re.IGNORECASE matches A == a
    Note: (?:something) this means do not capture this group
    """

    pattern = "(https?://)(?:www\.)?(youtu)(be)(\.com/embed)(/[a-zA-Z0-9]*)"
    result = re.search(pattern, s, re.IGNORECASE)
    if result == None:
        return None
    p1, p2, p3, p5 = result.group(1), result.group(2), result.group(3), result.group(5)
    """ if the length of 'p1' is 4 and missing the 's' sub the s in """
    # must add the s to http, == https
    if len(p1) == 4:
        p1 = re.sub("http", "https", p1)
    # sub the b in youtube with .b
    p3 = re.sub("b", ".b", p3)
    lst = list()
    # all the groups together to create the new link
    for n in (p1, p2, p3, p5):
        lst.append(n)
        result = "".join(lst)

        return result


if __name__ == "__main__":
    main()
