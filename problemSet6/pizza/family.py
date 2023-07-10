""" Module to ready CSV files """
with open("families.csv") as infile:
    for lines in infile:
        """ its
        row = lines.rstrip().split(',')
        print(row)