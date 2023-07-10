""" OOP encourages to have all of the methods related to that class incapsolated within the class """

class Student:
    """this initializes the content of the object"""
    def __init__(self, name, house):
        """ we can check if something exist, if not raise an error """
        if not name:
            raise ValueError("Missing name")
        if house not in ["Griffindoe", "Huffepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
            
        """attributes, instance variables"""
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    # assign an attribute to student object, name and house
    name = input("Name: ").lower()
    house = input("House: ").lower()
    # creating an object of the class, instantiating of a class
    return Student(name, house)


if __name__ == "__main__":
    main()
