""" Module to write a list of dictionary to a csv file """

import csv

# my data rows as dictionary objects
mydict =[{'branch': 'COE', 'cgpa': '9.0',
          'name': 'Nikhil', 'year': '2'},
        {'branch': 'COE', 'cgpa': '9.1',
         'name': 'Sanchit', 'year': '2'},
        {'branch': 'IT', 'cgpa': '9.3',
         'name': 'Aditya', 'year': '2'},
        {'branch': 'SE', 'cgpa': '9.5',
         'name': 'Sagar', 'year': '1'},
        {'branch': 'MCE', 'cgpa': '7.8',
         'name': 'Prateek', 'year': '3'},
        {'branch': 'EP', 'cgpa': '9.1',
         'name': 'Sahil', 'year': '2'}]
 
# field names
fields = ['name', 'branch', 'year', 'cgpa']

# name of csv file
filename = 'Uni_record.csv'

# write to csv file
with open(filename, 'w', newline='') as file:
    # create a csv dict writer object
    writer = csv.DictWriter(file, fieldnames = fields)
    #writing the header
    writer.writeheader()
    #writing data rows
    writer.writerows(mydict)
    
