""" working file """
import sys
import re

"""
    Script expects a str as time, in either 12-hour format or 24-hour format.
        * it returns str as a  time(24-format)
        * expect AM an PM will be capitalize( no periods therein)
        * assume that this time are representative of actual times
            FORMATS:
            9:00 AM to 5:00 PM
            9 AM to 5 PM
        * Raise a ValueError if the input to convert is not in the two formats given above
"""


def main():
    print(convert(input("Hours: ")))


def convert(s):
    """time(str) -> time(str)
    Returns the time in 24-hour format
    >>>convert("12 AM to 1:00 PM")
    00:00  to 13:00
    >>>convert("9 AM to 3 PM)
    09:00 to 15:00
    >>>convert("10:00 AM to 4:00 PM")
    10:00 to 16:00
    >>>convert("9 AM - 3:00 PM)
    None
    (\d{1,2})(?::?)(\d{0,2})\s([AP]M)(\sto\s)(\d{1,2})(?::?)(\d{0,2})\s([AP]M)
    """
    try:
        pattern = re.search(
            r"(\d{1,2})(?::?)(\d{0,2})?\s([AP]M)(\sto\s)(\d{1,2})(?::?)(\d{0,2})?\s([AP]M)", s
        )

        if pattern:
            raise ValueError("Invalid time")

    except ValueError:
        pass
    """ Note: t1 == first hour entry
              t1_m1 == first hour minutes
              t2 == second hour entry
              t2_m2 == second hour minutes
    """
    t1, t1_min, t2, t2_min, hr1, sp, hr2 = [
            int(pattern.group(1)),
            int(pattern.group(2)) if pattern.group(2)  else 0,
            int(pattern.group(5)),
            int(pattern.group(6)) if pattern.group(6)  else 0,
            pattern.group(3),
            pattern.group(4),
            pattern.group(7),
            ]
    # times = [int(t1), int(t2)]
    # time = (int(n) for n in (t1,t2))
    """
        NOTE: add a zero infront re.sub(r'^(\d)$', r'0\1', str(t1))
    """
    """ convert time to 24-hour clock t1"""
    if (hr1 == 'PM') and (t1 != 12):
        t1+= 12
    elif (hr1 == 'AM') and (t1 == 12):
        t1 = 0
    """ convert time to 24-hour clock t2 """
    if (hr2 == 'PM') and (t2 != 12):
        t2+= 12
    elif (hr2 == 'AM') and (t2 == 12):
        t2 = 0

    """ add a zero in front of time """
    if (len(str(t1)) < 2):
        t1 = F"0{t1}"
    if (len(str(t2)) < 2):
        t2 = F"0{t2}"

    return F"{t1}:{t1_min:02d}{sp}{t2}:{t2_min:02d}"

if __name__ == "__main__":
    main()
