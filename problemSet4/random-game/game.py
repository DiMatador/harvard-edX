""" number guessing game, input number from user and game will generate a random number for the user to guess """

import random

# main function
def main():
    play_game = random_game()
    return play_game


def random_game():

    while True:
        power_up = input("Power:")

        try:
            int(power_up)
        except ValueError:
            continue
        break

    power_up = int(power_up)

    powerBall = random.randint(1, power_up)
    while True:
        user_guess = int(input("Guess: "))
        try:
            # user_guess = int(input("Guess: "))

            # powerBall = random.randint(1, power_up)
            if powerBall == user_guess:
                print("We got a winner!!")
                break
            elif powerBall != user_guess and user_guess < powerBall:
                print("Guess to low!")

            elif powerBall != user_guess and user_guess > powerBall:
                print("Guess to high")

        except ValueError:
            pass

        pass

main()
