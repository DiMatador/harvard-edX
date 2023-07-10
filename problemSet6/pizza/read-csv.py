''' read a csv file '''

# create a list to add the dictionary to items
families= list()
with open ("families.csv") as infile:
    for line in infile:
        name, house = line.rstrip().split(",")
        # create a dictionary and create keys with names and house names
        family = {"name": name, "house": house}
        # append the dictionary family to list families, stay organazed
        families.append(family)
        
# use a function
# create a function to get student dictionary
def get_house(family):
    # note that the function is returning the "house" from the dictionary
    return family["house"]
    
    
# loop to return a sorted dict.. here we pass the function to sorted()
for family in sorted(families, key=get_house):
    print(F"{family['name']} is in {family['house']}")
       