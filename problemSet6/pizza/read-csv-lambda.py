''' module read csv. here we are gonna use lambda instead of a function '''
# this is a more clean way of doing items
# lanbda is a unanimous function
# create an empty list
students = list()

# open the csv file
with open("students.csv") as infile:
    # loop through the infile
    for lines in infile:
        # split returns a list, assigned, name and house 
        name, house = lines.rstrip().split(",")
        # use the list returned by split and assign the values as keys to a dictionary
        student = {"name": name, "house": house}
        # now append the student dictionaries to the list above
        students.append(student)
        
''' here we gonna use lambda instead of creating a function and returning one of the keys from the list of dictionaries '''
# loop and sort
for student in sorted(students, key=lambda student: student["name"]):
    print(F"{student['name']} is in {student['house']}")