""" Module pizza. problem set 6 """

import sys
import csv
from sys import argv
from tabulate import tabulate

""" module to read and print a csv file. print it with tabulate tables format """
items = list()
try:
    module, file = argv
    if file.endswith(".csv") == False:
        sys.exit("Not a CSV file")
except ValueError:
    # check, argv length 2
    if len(argv) < 2:
        sys.exit("Too few command-line arguments")

    # check, argv length is greater than 2
    if len(argv) > 2:
        sys.exit("Too many command-line arguments")
else:
    pass


try:
    with open(argv[1]) as infile:
        # DictReader object to read data
        reader = csv.DictReader(infile)

        # use tabulate table='grid' to display the table
        print(tabulate(reader, headers="keys", tablefmt="grid"))


except FileNotFoundError:
    # if the file does not exit 
    sys.exit("File does not exist")