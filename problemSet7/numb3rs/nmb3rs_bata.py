import re
import sys

"""this is a bata script for numb3rs.py"""

def main():
    # expect an IPv4 as a (str)
    print(validate(input("IPv4 Address: ")))


""" working function"""
def validate(ip):
    """
        expect an IPv4 address as input (str)
        IPv4 as #.#.#.# each # should be a number between 0 and 255
        returns True or False, if valid or not 
    """
    # IPv4 as #.#.#.#
    
    try:
    except ValueError:
        pass
    
if __name__ == "__main__":
    main()