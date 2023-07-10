""" bata file for assignment jar """
import sys
import re

class Jar:
    def __init__(self, capacity=12):
        """ Note the max number of cookies that can go in the jar '12', if capacity is a
        non-negative int
        It should instead raise a ValueError
        """
        self.capacity = capacity
        if capacity < 0:
            raise ValueError("Jar capacity cannot be negative")
        

    def __str__(self):
        """str -> str
        Returns a str
        """
        return F"testing the result, {self.capacity}"

    def deposit(self, n):
        """int -> int(n cookies)
        Return the number of cookies deposited in the cookie jar,
        raise ValueError if the capacity is exceeded
        """
        

    def withdraw(self, n):
        """Removes the n cookies from the cookie jar,
        if there aren't that many cookies in the cookie jar,
        raise ValueError
        """


    @property
    def capacity(self):
        """Returns the cookie jar capacity"""
        # remove the n number of cookies from the capacity


    @property
    def size(self):
        """ SETTER.... Return the number of cookies actually in the cookie jar """
        # Validation or manipulation can be done here
        # before setting the attribute



def main():
    """
    Returns the number of cookies in the jar, cookies deposited, cookies removed.
    raises exception if a negative cookie is attempted
    """
    cookie = input("cookies ")

    # Create an instance of Jar
    cookie_monster = Jar(cookie)
    print(cookie_monster)


if __name__ == "__main__":
    main()