""" write csv with headers and given info """

import csv

# field names
fields = ['Name', 'Branch', 'Year', 'CGPA']
 
# data rows of csv file
rows = [ ['Nikhil', 'COE', '2', '9.0'],
        ['Sanchit', 'COE', '2', '9.1'],
        ['Aditya', 'IT', '2', '9.3'],
        ['Sagar', 'SE', '1', '9.5'],
        ['Prateek', 'MCE', '3', '7.8'],
        ['Sahil', 'EP', '2', '9.1']]

# name of csv file
filename = 'students.csv'

# write to csv file
with open(filename, 'w', newline='') as csvfile:
    #create a csv writer object
    writer = csv.writer(csvfile)
    #write to the file
    writer.writerow(fields)
    # writing the data rows
    writer.writerows(rows)
    
print(writer)