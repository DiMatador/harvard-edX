import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    """
    (str) -> str
    Returns a shorter version of a Youtube like.
    >>> parse(<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>"
    http://youtu.be/xvFZjo5PgG0
    >>> parse("<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0"
    title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
    encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>")
    https://youtu.be/xvFZjo5PgG0
    >>> parse("http://www.youtube.com/embed/xvFZjo5PgG0")
    None
    >>> parse("<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>")
    None
    """

    # use RE to search the link str and return None if str is None
    pattern = r"(https?://)(?:www\.)?(youtu)(be)(\.com/embed)(/[a-zA-Z0-9]*)"
    result = re.search(pattern, s, re.IGNORECASE)
    if result == None:
        return None

    # check  if iframe exist in the link str
    if (not s.startswith("<iframe")) and (not s.endswith("></iframe>")):
        return None

    # break the link str into groups
    p1, p2, p3, p5 = result.group(1), result.group(2), result.group(3), result.group(5)

    # add the s to http, == https
    if "s" not in p1:
        p1 = re.sub("http", "https", p1)

    # add '.' in between youtube == 'youtu.be'
    p3 = re.sub(r"(b)", r".\1", str(p3))

    # create the link
    lst = list()
    for n in (p1, p2, p3, p5):
        lst.append(n)
        result = "".join(lst)

    return result


if __name__ == "__main__":
    main()
