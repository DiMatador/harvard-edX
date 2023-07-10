#==========counting with dictionaries==============
#===histagram===
# create a dict
counts = dict()

# list of names
names = ['julio', 'jordi', 'jaxx', 'diana', 'jaxx', 'diana', 'jordi', 'jaxx']

# loop through the names list
for name in names:
    # if we have not seen the name set it to 1
    if name not in counts:
        counts[name] = 1
    # if the name is already in the dict than add one
    else:
        counts[name] = counts[name] + 1

print(counts)

# method to count, if we have not seen the name before, store it. if we see it again add '1' to it
if name in counts:
    x = counts[name]
else:
    x = 0
x = counts.get(name, 0)# the zero here gives us a default number so there is no trase back
print(f"get the highest count: {name} {x}")
