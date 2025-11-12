""" 
I acknowledge the use of
Microsoft Copilot (version GPT-4, Microsoft, https://copilot.microsoft.com/)
to create the code in this file 
"""
import random

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            if not 1 <= guess <= 100:
                print("Please guess a number between 1 and 100.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} tries.")
            break

if __name__ == "__main__":
    play_game()

