def main():
    time = convert(input("What time is it? "))
    print(time)


def convert(time):
    """str > str
    Return the meal accourding to time
    >>>convert('12:00')
    "lunch time"
    >>>convert('18:00')
    "dinner time"
    >>>convert('8:00')
    "breakfast time"
    """
    hour, minutes = time.split(':')
    if hour >= '7' and time <= '8':
        return "Breakfast time"
    elif hour >= '12' and hour <= '13':
        return "lunch time"
    elif hour >= '18' and time <= '19':
        return "Dinner time"

main()