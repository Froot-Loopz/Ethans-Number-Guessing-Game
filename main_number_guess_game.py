import random
import art
print(art.logo )
print("---- Welcome To Ethans Number Guessing Game ----")


def easy_mode():
    game_over = False
    attempts = 10
    random_number = random.randint(1,100)
# While loop created to run the 'easy' game mode functions
    while not game_over:
        if attempts == 1:
            game_over = True
# check attempts remaining & if user wants to play_again
        guess = input("Guess a number between 1 and 100: ")
        if int(guess) != random_number and attempts == 1:
            game_over = True
            print(f"You ran out of guesses! The number was {random_number}")
            play_again = input("Would you like to play again? Type 'y' or 'n': ").lower()
            if play_again == "y":
                easy_mode()
            else:
                print("Thanks for playing! Goodbye!")
                game_over = True
# Correct guess check, and play_again check
        elif int(guess) == random_number:
            print(f"You Got It! The number was {random_number}\n")
            play_again = input("Would you like to play again? Type 'y' or 'n': ").lower()
            if play_again == "y":
                easy_mode()
            else:
                print("Thanks for playing! Goodbye!")
                game_over = True
# Too high check
        elif int(guess) > random_number:
            print("Too high!\n")
            attempts -= 1
            print(f"You have {attempts} attempts left")
# Too low check
        elif int(guess) < random_number:
            print("Too low! \n")
            attempts -= 1
            print(f"You have {attempts} attempts left")



def hard_mode():
    game_over = False
    attempts = 5
    random_number = random.randint(1,100)
# While loop created to run the 'easy' game mode functions
    while not game_over:
        if attempts == 1:
            game_over = True
# check attempts remaining & if user wants to play_again
        guess = input("Guess a number between 1 and 100: ")
        if int(guess) != random_number and attempts == 1:
            game_over = True
            print(f"You ran out of guesses! The number was {random_number}")
            play_again = input("Would you like to play again? Type 'y' or 'n': ").lower()
            if play_again == "y":
                game_mode()
            else:
                print("Thanks for playing! Goodbye!")
                game_over = True
# Correct guess check, and play_again check
        elif int(guess) == random_number:
            print(f"You Got It! The number was {random_number}\n")
            play_again = input("Would you like to play again? Type 'y' or 'n': ").lower()
            if play_again == "y":
                game_mode()
            else:
                print("Thanks for playing! Goodbye!")
                game_over = True
# Too high check
        elif int(guess) > random_number:
            print("Too high!\n")
            attempts -= 1
            print(f"You have {attempts} attempts left")
# Too low check
        elif int(guess) < random_number:
            print("Too low! \n")
            attempts -= 1
            print(f"You have {attempts} attempts left")



def game_mode():
    easy_or_hard = input("Would you like to play on 'easy' or 'hard' mode? ").lower()
    if easy_or_hard == "easy":
        easy_mode()
    else:
        hard_mode()



game_mode()
