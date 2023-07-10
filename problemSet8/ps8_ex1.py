""" here the get_student returns a list, lists are mutable, can be change"""
def main():
    """ prints the return values from get_student """
    student = get_student()
    # lets say that we know from what house a student is from
    # wrong house was give, we can correct it here
    if student[0] == 'Padma'.lower():
        # this assignment works because we are getting a list in return
        student[1] = 'Ranvenclaw'
    print(F"{student[0]} from {student[1]}")


def get_student():
    """ str -> str
    Returns the name and home of a student
    >>> get_student('Jaxx')
    Jaxx 
    >>> get_student('Davila')
    Davila
    """
    name = input("Name: ")
    house = input("House: ")
    # remember to change the return here if we have '()' or no brackets its a Tuple, Tubles are inmutable
    # if we enclose them in '[]' we have a list, a list is mutable 
    return [name, house]
    


if __name__ == "__main__":
    main()