# script: coke machine
# main funcion
def main():

    calculate_payment()



#=============================================================================================
# Logical function
def calculate_payment():
    m = 0
    price = 50
    coins = [5, 10, 25]

    # Owed amount calculated
    while price != 0:
        print("Amount Due: ", price)
        m = int(input("Insert Coin: "))
        if m not in coins:
            # print("not valid")
            continue
        if price > m:
            price = price - int(m)
            #print("Amount Due: ",price)
        else:
            price = m - price           

    print("Amount Owed: ",price)



# main function call
main()



#here the program quits at Change Owed 10
# script: coke machine
# main funcion
# def main():
    # calculate_payment()

# #=============================================================================================

# # Logical function
# def calculate_payment():
    # m = 0
    # price = 50
    # coins = [5, 10, 25]

    # # Owed amount calculated
    # while price > 0:
        # print("Amount Due: ", price)
        # m = int(input("Insert Coin: "))
        # # validate coin
        # if m not in coins:
            # continue;
        # # calculate the price
        # if (price > m):
            # price = price - m
            # #print("Amount Due: ",price)
        # else:
            # price = m - price
            # print("Amount Owed: ",price)
            # break;

# main()