
def main():
    answer(input("What is the Answer to the Greatest Question of life, the Universe, and Everything? "))


# logical function
def answer(n):
    """str > str
    Returns a answer as a string, the answer is 42, forty-two, Forty Two
    >>>answer("Nope")
    >>>answer("42")
    "Yes"
    >>>answer("forty-two")
    "Yes"
    >>>answer("forty two")
    "Yes"
    >>>answer("Forty Two")
    "Yes"
    """
    n = n.strip().lower()
    if n == str('42') or n == 'forty two':
        print("Yes")
    elif n == 'forty-two':
        print("Yes")
    else:
        print("No")


main()