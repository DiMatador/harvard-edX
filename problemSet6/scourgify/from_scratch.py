# Customizing the Delimeter In Python CSV Files
import csv

headers = ['Name', 'Age', 'Website', 'Location']

values = [
    {'Name': 'Nik', 'Age': 34, 'Website': 'datagy.io'},
    {'Website': 'google', 'Name': 'Kate', 'Age': 33},
]

with open('dicttocsv.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=headers, delimiter=",")
    writer.writeheader()
    writer.writerows(values)


#=============================================================================================