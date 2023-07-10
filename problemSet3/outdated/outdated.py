
# main function
def main():
    run = date("Date: ")
    return(run)


# logical function
def date(prompt):
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

    ''' loop until we unwrap the date'''
    while True:
        user = input(prompt)
        try:
            month, day, year = user.split('/')
            if int(month)>=1 and int(month) <= 12 and int(day) >= 1 and int(day) <= 31:
                break
        except:
            
            try:                
                mensis, die, annus = user.split(' ')
                for m in range(len(months)):
                    if mensis == months[m]:
                        mensis = m +1

                new_die = die.replace(",", "")

                if int(month)>=1 and int(month) <= 12 and int(day) >= 1 and int(day) <= 31:
                    break
            except:
                
                pass
            pass
        
    return(F"{year}-{int(month):02}-{int(day):02}")     

# call main
if __name__ == "__main__":
    main()

     
