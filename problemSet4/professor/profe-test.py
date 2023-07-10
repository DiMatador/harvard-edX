from random import randint


def main():
    level = get_level()
    game = play_game(level)
    print(game)


""" generate a level """
def get_level():
    
    #level = 0
    levels = [1,2,3]
    while True:
        try:
            user = input("Level: ")
            level = int(user)
            if level not in [1,2,3]:
                continue
            else:
                return level
        except (ValueError,TypeError):
            pass
            
    return level
    
    
#==========================================================================   


""" generate a random number """
def generate_interger(level):
    x,y = 0,0
    
    if level == 1:
        x = randint(0, 9)
        y = randint(0, 9)
        return x,y 
    if level == 2:
        x = randint(10, 99)
        y = randint(10, 99)
        return x,y
    if level == 3:
        x = randint(100, 999)
        y = randint(100, 999)
        return x,y
        
    return x,y
    
#==========================================================================

""" generate errors """
def generate_error(x, y):
    ct = 0
    error = "EEE"
    while ct < 3:
        
        try:
            total = x + y
            user = int(input(F"{x} + {y} = "))
            if user == total:
                return True
            if user != total:
                ct+=1
                print(error)
        except (ValueError, TypeError):
            print(total)
        ct+=1
    return False


#==========================================================================

def play_game(level):
    score = 0
    ct = 0
    while ct < 10:
        x, y = generate_interger(level)
        errors = generate_error(x, y)
        if errors == False:
            ct+=1
            pass
        else:
            score+=1
            
        ct+=1
        
    return ct
if __name__ == "__main__":
    main()  