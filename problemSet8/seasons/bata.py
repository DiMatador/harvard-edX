""" Assignment seasons """
from datetime import date, datetime
import inflect
import operator
import sys
import re


class CheckDate:
    """int -> str(date)
    Return a given birth date as a st, calculates the number of minuts that have pass since you were born
    >>> CheckDate(2022-05-11)
    'Five hundred twenty-five thousand, six hundred minutes'
    """

    def __init__(self, birth_date):
        self.birth_date = birth_date

    """ function to calculate the number of minutes in a birthdate """

    def minutes_in_birthday(self):
        n2w = inflect.engine()
        # extract year, month and day
        year, month, day = map(int, self.birth_date.split("-"))

        # assign year, month and day to variables
        birthdate = date(year, month, day)

        # today date
        td = date.today()

        # convert today date to midnight
        midnight_today = datetime.combine(td, datetime.min.time())

        # convert birthdate to midnight time
        birth_at_midnght = datetime.combine(birthdate, datetime.min.time())

        # calculate the number of days in birthdate
        difference = operator.sub(midnight_today, birth_at_midnght)
        minutes = difference.total_seconds() // 60

        in_words = n2w.number_to_words(round(minutes))
        #birthdate_in_words = in_words

        # remove the 'and' and extra spaces
        if ' and ' in in_words:
            pattern = re.compile(r"\s\band\s\b")
            in_words = re.sub(pattern, ' ', in_words)


        return F"{in_words.capitalize()} minutes"


def main():
    """int -> str(birth date)
    Prints the number of minutes that have pass in a birthday
    """

    birth_date = input("What is your birth date? ")

    pattern = "^\d{4}-\d{2}-\d{2}$"
    if not re.match(pattern, birth_date):
        sys.exit("Invalid date")

    # object
    date_check = CheckDate(birth_date)
    print(f"{date_check.minutes_in_birthday()}")

    sys.exit(0)

if __name__ == "__main__":
    main()
