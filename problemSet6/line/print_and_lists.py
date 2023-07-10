''' if we want to add info to a file and edite that file in the future, we
can use a list to store and and edit the list as we need to '''

# list
names = list()

with open('names.txt') as infile:
    for line in infile:
        names.append(line.rstrip())

''' once we have eterated through the file and add it the items to a list
we can use a for loop to print a sorted list. this makes it easy to use'''
for name in sorted(names):
    print(F"Hello, {name}")