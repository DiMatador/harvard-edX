def main():
    payment = calculate_payment()
    print(payment)


def calculate_payment():
    """str > int
    Returns the calculated price of a coke, coke price is 50c.
    the machine only accpets 25c, 10c and 5c
    >>>calculate_payment("25")
    25
    >>>calculate_payment("10")
    15
    >>>calculate_payment("5")
    10
    """
    price = 50
    coins = [25, 10, 5]
    while price > 0:
        print(F"Amount due: {price}")
        m = int(input("Insert coin: "))
        # validate the coin inserted
        if int(m) not in coins:
            continue
        # calculate the price
        if price > m:
            price -= m
        else:
            price -= m
            break

    return F'Change Owed: {price}'


main()
