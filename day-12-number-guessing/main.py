import random
from art import logo


def compare(guess, answer, attempts):
    if guess > answer:
        if attempts > 1:
            return "Too high.\nGuess again."
        else:
            return "Too high."
    elif guess < answer:
        if attempts > 1:
            return "Too low.\nGuess again."
        else:
            return "Too low."
    else:
        return "You got it!"


def set_difficulty(attempts,  secret_number):
    while attempts > 0:
        if attempts == 1:
            print(f"You have {attempts} attempt remaining to guess the number.")
        else:
            print(f"You have {attempts} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))
        print(compare(guess, secret_number, attempts))

        if guess == secret_number:
            print(f"The answer was {secret_number}")
            return

        attempts -= 1

    print("You've run out of guesses, you lose.")


def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    secret_number = random.randint(1, 100)

    # print(f"Pssst, the correct answer is {secret_number}")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()

    if difficulty == "easy":
        set_difficulty(10, secret_number)

    elif difficulty == "hard":
        set_difficulty(5, secret_number)


play_game()