# simplified counting with get
# get only works with dictionaries

counts = dict()
names = ['julio','jaxx', 'jordi', 'jaxx', 'diana', 'jaxx', 'diana', 'jordi', 'jaxx']

# loop to count the number of names
for name in names:
    # get the name and add one everytime the loop goes around
    counts[name] = counts.get(name, 0) + 1
    # x keeps track of how many times the name appears
    x = counts[name]
# print the name that appears the most
print(f"The name with the hieghest count is: {name} {x}")
