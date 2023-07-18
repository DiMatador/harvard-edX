def main():
    phrase = camel(input("Camel case: "))
    print(phrase)


def camel(m):
    on_split = ''
    # iterate over the m snake case given str
    for upper_case in m:
        # check if there is an upper case character
        if upper_case.isupper():
            # if an upper case is found keep the first word add '^' and first letter of next word
            on_split += '^' + upper_case
            # if upper case letter found make it lower case
            on_split = on_split.lower()
        else:
            # keep on adding characters to on_plit
            on_split += upper_case

    # remove the '^'
    on_split = on_split.split('^')
    # put it all together
    camel_case = '_'.join(on_split)

    return camel_case


main()
