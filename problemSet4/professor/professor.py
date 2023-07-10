import random

# main function
def main():
    get_level = generate_level()
    play = generate_game(get_level)
    return F"Score: {play}"


# ============================================
''' generate a level from 1 to 3 '''
def generate_level():
    """(int) -> int
    Returns a level between number 1, 2 and, 3
    gen_level() 4
    >>> Level: 2
    2
    >>> gen_level() 3
    3
    """
    ''' loop until the right level number is entered '''
    while True:
        level = input("Level: ")
        try:
            level = int(level)
            if level in [1,2,3]:
                break
        except (ValueError, TypeError):
            pass

    return level

# ============================================
''' Generate random integers '''
def generate_integer(level):
    """(int) -> int
    Returns a random generated integer from (0-9,0-9), (10-99,10-99) and (100-999, 100-999),
    useing the variables x and y
    x = random.randint(0,10)
    >>> 1
    y = random.randint(0,10)
    >>> 7
    """
    x, y = 0, 0
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        return x, y

    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
        return x, y

    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
        return x, y

    return x, y

# =============================================
''' Check for 3 errors '''
def generate_error(x, y ):
    ''' allow for 3 errors, loop to catch all 3 errors '''
    wrong = "EEE"
    error = 0
    while error < 3:
        result = x + y        
        try:
            user =  int(input(F"{x} + {y} = "))
            if user == result:
                return True
            else:
                error+=1
                print(wrong)               
        except ValueError:
            error+=1
            
    print(result)
    return False
# ============================================
''' Generate the game '''
def generate_game(level):
    ct = 0
    total = 0
    while ct < 10:
        x, y = generate_integer(level)
        user_error = generate_error(x, y)
        if user_error == True:
            total+=1
        ct+=1

    return total

if __name__ == "__main__":
    main