import random

# definition of function for guessing game


def guessing_game():
    print("Welcome to my guessing game! ")
    print("\'The rules are simple guess an integer between 1 - 100 in as least tries as possible.\'\n")
    game_start = input("Would you like to play? (yes/no) ").lower()

    if game_start == "yes":
        rand_num = random.randint(1, 101)
#        print(rand_num)

        user_guess = int(input("\nGuess a number 1 - 100: "))
        guess_count = 1

        while user_guess != rand_num:
            if (user_guess > 0) and (user_guess <= 100):
                if user_guess < rand_num:
                    user_guess = int(input("Your guess is too low, try again: "))
                elif user_guess > rand_num:
                    user_guess = int(input("Your guess is too high, try again: "))
            else:
                user_guess = int(input("Guess is out of range, try again: "))

            guess_count += 1

        if user_guess == rand_num and guess_count == 1:
            print("\nCongratulations! You guessed the correct number!\nIt took you", guess_count, "try.\n")
        elif user_guess == rand_num:
            print("\nCongratulations! You guessed the correct number!\nIt took you", guess_count, "tries.\n")

        play_again = input("Would you like to play again? (yes/no) ").lower()
        print()
        if play_again == "yes":
            guessing_game()
        else:
            print("Thanks for playing! ")
    else:
        print("Alright, maybe next time...")


guessing_game()
