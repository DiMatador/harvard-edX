""" Module pizza. problem set 6 """

import sys
import csv
from sys import argv
from tabulate import tabulate

# list
items = []
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
        print(tabulate(reader, headers="keys", tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")


""" here we can do it using the reader and not the DictReader method
# DictReader object to read data
        reader = csv.reader(infile)
        # for row in reader:
            # items.append(row)
        # print(tabulate(items[1:], headers=items[0], tablefmt='grid'))
"""
