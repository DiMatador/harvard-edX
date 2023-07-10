''' script to convert USA date system '''

# main function
def main():
    ''' function -> date str
    Return the function date_Convert(prompt) date
    '''
    new_date = date_Converter('Date: ')
    return(new_date)

# logical function
def date_Converter(prompt):
    ''' (number-date-str) -> int-str
    >>> 05/08/1973
    1973-08-05
    >>> May 25, 1975
    1975-5-25
    Return the date as meiddle-endian(YY-MM-DD) from anno Domini(9/8/1636 or
    September 8, 1636) date_Converter(prompt)
    '''
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    
    lst = []

    while True:
        try:
            new_date = input(prompt).title()
        except (EOFError):
            break

        try:
            corte = new_date.split()
            print(corte)
            rev = corte[::-1]
            print(rev)
        except (NameError):
            pass

        break
        
# call main
main()









