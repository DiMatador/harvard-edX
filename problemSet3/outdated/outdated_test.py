# main function
def main():
    date = get_date("Date: ")
    return date


# logical function
def get_date(prompt):
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
        "December",
    ]

    while True:
        user = input(prompt)
        try:
            """split and check the len of the day"""
            month, day, year = user.split("/")
            if (
                int(month) >= 1
                and int(month) <= 12
                and int(day) >= 1
                and int(day) <= 31
            ):
                break

        except:
            try:
                """look for month in the months list"""
                mon, d, year = user.split(" ")
                for m in range(len(months)):
                    if mon == months[m]:
                        month = m + 1

                day = d.replace(",", "")
                """ check month and day """
                if (
                    int(month) >= 1
                    and int(month) <= 12
                    and int(day) >= 1
                    and int(day) <= 31
                ):
                    break
            except:
                pass

    print(f"{year}-{int(month):02}-{int(day):02}")


""" call main """
if __name__ == "__main__":
    main()
