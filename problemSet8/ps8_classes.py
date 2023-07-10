class Student:
    """this initializes the content of the object"""

    def __init__(self, name, house):
        """attributes, instance variables"""
        self.name = name
        self.house = house


def main():
    student = get_student()
    if student.name == "Padma":
        student.house == "Ravenclaw"
    print(f"{student.name} from {student.house}")


def get_student():
    # assign an attribute to student object, name and house
    name = input("Name: ").lower()
    house = input("House: ").lower()
    # creating an object of the class, instantiating of a class
    return Student(name, house)


if __name__ == "__main__":
    main()
