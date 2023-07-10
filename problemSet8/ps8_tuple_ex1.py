""" get_student is returning a tuple, 
    tuples are inmutable
"""
def main():
    """ prints the return values from get_student """
    student = get_student()
    
    # here we can access the items in the tuple just like we do in a list
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
    
    # the return statement will return a tuple when we return values separated by comma
    # '()' or no brackets its a Tuple, Tubles are inmutable
    # if we enclose them in '[]' we have a list, a list is mutable 
    return (name, house)
    


if __name__ == "__main__":
    main()