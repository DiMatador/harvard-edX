""" problem set 6 assignment Scourgify.py """
# imports
import csv
import sys
from sys import argv

data = list()
""" Module to writer from one csv file to a new file. separate first_names, last_names and house """
try:
    module, read_file, write_file = argv
    # not csv file exit
    if read_file.endswith(".csv") == False:
        sys.exit("Not a CSV file")
except ValueError:
    if len(argv) > 3:
        sys.exit("Too many command-line arguments")
    if len(argv) < 3:
        sys.exit("Too few command-line arguments")
else:
    pass

try:
    """read csv file"""
    data = list()
    with open(argv[1], newline="") as csv_read_file:
        # DictReader() returns an ordered dictionary
        reader = csv.DictReader(csv_read_file)
        for row in reader:
            # split on the first comma and space
            col = row["name"].split(", ")
            # create the header columns to pass to write
            data.append(
                {
                    "first": col[1].rstrip(),
                    "last": col[0].rstrip(),
                    "house": row["house"],
                }
            )
            
            
        """ write csv file """
        headers = ["first", "last", "house"]
        with open(argv[2], "w", newline="") as csv_write_file:
            writer = csv.DictWriter(csv_write_file, fieldnames=headers)
            # create a header
            writer.writeheader()
            # this creates the columns heading
            """writer.writerow({"first": "first", "last": "last", "house": "house"})"""
            # write the new CSV file, we need to write the headers that way they get imported
            for row in data:
                # create 3 colomns
                writer.writerow(
                    {"first": row["first"], "last": row["last"], "house": row["house"]}
                )


except FileNotFoundError:
    sys.exit("File does not exist")

else:
    pass

"""
1) Expects the user to provide two command-line arguments:
the name of an existing CSV file to read as input, whose columns are assumed to be,
in order, name and house.
the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.

2) Converts that input to that output, splitting each name into a first name and last name. Assume that
each student will have both a first name and last name.

3) If the user does not provide exactly two command-line arguments, or if the first cannot be read, 
the program should exit via sys.exit with an error message.
"""
