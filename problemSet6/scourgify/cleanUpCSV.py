"""Module to clean all puntuations from a csv file"""
import csv


students = list()
dict_lst = list()

with open("before.csv", newline='') as read_csv:
    reader = csv.DictReader(read_csv, delimiter='"')
    for lines in read_csv:
        name,house = lines.rstrip().split()
    # each row is a dictionary
    for row in reader:       
        # list of dictionaries
        students.append(row)
        
    # dictionary
    for keys, values in row.items():
        students.append(keys)
        print(keys)
        dict_lst.append(row)
        print(values)
        
    # write a header, this works
    #headers = ['name', 'last', 'house']        
    # with open("new.csv", 'w', newline='') as write_csv:
        # fieldnames = 'name', 'last', 'house'
        # writer = csv.DictWriter(write_csv, fieldnames = fieldnames)
        # writer.writeheader()
        # writer.writerow(row)
        