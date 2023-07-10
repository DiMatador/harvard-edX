""" here we are going to use a dictionary to ready the csv file """

import sys
import csv
from sys import argv
from tabulate import tabulate


# list to store values
items = list()

""" check the number of arguments pass to command-line """
try:
    module, file = argv
    if file.endswith(".csv") == False:
        sys.exit("Not a CSV file format")
except ValueError:
    if len(argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(argv) > 2:
        sys.exit("Too many command-line arguments")
else:
    pass
    
""" check that the file exist.
Here we are going to use dictionary to open the csv file """
try:
    with open(argv[1], newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['Cisilian'],row['small'], row['large'])
except FileNotFoundError:
    sys.exit("File does not exist")