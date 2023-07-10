
""" in this example, get_student is returning a dict"""
def main():
    # assign a variable to the get_student()
    student = get_student()
    # correct the right house for Padma if entered wrong
    if student["name"] == "Padma".lower():
        student["house"] = "Ravenclaw"
        
    # print the write information
    print(F"{student['name']} from {student['house']}")


def get_student():
    """ str -> str, dict
    Returns the name and home of a student
    >>> get_student('Jaxx')
    Jaxx 
    >>> get_student('Davila')
    Davila
    
    this example returns a dict 
    """
    # # student dict
    # student = {}
    # # assign keys to name and house
    # student["name"] = input("Name: ")
    # student["house"] = input("House: ")
    # return student
    """ we can return a dict directly, more compact way if doing it than what we got above 
        Note: we create the name and house veriables in situ
    """
    
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}


if __name__ == "__main__":
    main()