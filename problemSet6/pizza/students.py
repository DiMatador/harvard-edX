''' module to open and ready a csv file, print the file ordered '''
# using a function to pass to sorted

# list to store the dictionary of students
students = list()
with open("students.csv") as infile:
    for line in infile:
        # split() returns a list, assign items from csv file to name and house
        name, house = line.rstrip().split(",")
        # create a dictionary to add the list to items
        student = {"name": name, "house": house}
        students.append(student)
        
# function: returns the student name from the dictionary
def get_student(student):
    # function returns the student key
    return student["name"]

# loop through the list students
# get_student() gives us the students name key to sort by
for student in sorted(students, key=get_student):
    print(F"{student['name']} is in {student['house']}")