from datetime import date, datetime
import inflect
import sys
import re


class CheckDate:
    """str -> str(date)
    Return a given birth date as a str, calculates the number of minuts that have pass since you were born
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

        """
            Assign year, month and day to variables. date() function could raise a ValueError
        """
        try:
            birthdate = date(year, month, day)
        except ValueError:
            sys.exit("Invalid date")

        # todays date
        today = date.today()

        # convert today date to midnight time today
        midnight_today = datetime.combine(today, datetime.min.time())

        # convert birthdate to midnight time
        birth_at_midnght = datetime.combine(birthdate, datetime.min.time())

        # extract the difference between birthdate and today date
        difference = midnight_today - birth_at_midnght
        minutes = difference.total_seconds() // 60

        # round and pass the minutes as words to a variable
        in_words = n2w.number_to_words(round(minutes))

        # Remove 'and' from the output, replace with empty string
        if ' and ' in in_words:
            pattern = re.compile(r"\s\band\s\b")
            in_words = re.sub(pattern, ' ', in_words)

        return F"{in_words.capitalize()} minutes"


def main():
    """ str -> str(birth date)
    Prints the number of minutes that have pass in a birthday
    """

    birth_date = input("What is your birth date? ")

    pattern = "^\d{4}-\d{2}-\d{2}$"
    if not re.match(pattern, birth_date):
        sys.exit("Invalid date")

    # object
    check_my_birthdate = CheckDate(birth_date)
    print(f"{check_my_birthdate.minutes_in_birthday()}")

    return 0

if __name__ == "__main__":
    main()
