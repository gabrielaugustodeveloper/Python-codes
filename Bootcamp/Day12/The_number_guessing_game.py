from art import logo
import random

def check_guess(guess, answer):
    if guess > answer:
        print("Too high!")
    elif guess < answer:
        print("Too low!")
    elif guess == answer:
        print("You guessed right!!!!")

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return 10
    else:
        return 5
def game(attempts):
    answer = random.randint(1,100)

    while attempts > 0:
        print(f"\nYou have {attempts} attempts remaining.")
        guess = int(input("Make a guess: "))

        if guess == answer:
            check_guess(guess, answer)
            return  # End the game if correct

        check_guess(guess, answer)
        attempts -= 1

    print(f"\nYou've run out of guesses. The answer was {answer}.")


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
attempts = set_difficulty()
game(attempts)
