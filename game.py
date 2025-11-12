""" 
I acknowledge the use of
Microsoft Copilot (version GPT-4, Microsoft, https://copilot.microsoft.com/)
to create the code in this file.

Guess the Number Game
---------------------
A simple text-based game where the player tries to guess a random number.
Includes input validation, replay option, and scoring system.
"""

import random

def choose_difficulty():
    """Ask the user to choose a difficulty level."""
    print("\nSelect difficulty level:")
    print("1. Easy (1–50)")
    print("2. Medium (1–100)")
    print("3. Hard (1–200)")

    while True:
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice == "1":
            return 1, 50
        elif choice == "2":
            return 1, 100
        elif choice == "3":
            return 1, 200
        else:
            print("⚠️ Please choose a valid option (1, 2, or 3).")


def play_game():
    """Plays one round of Guess the Number."""
    low, high = choose_difficulty()
    number_to_guess = random.randint(low, high)
    attempts = 0

    print(f"\n🎲 Welcome to Guess the Number ({low}–{high})!")
    print(f"I'm thinking of a number between {low} and {high}.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            if not low <= guess <= high:
                print(f"⚠️ Please guess a number between {low} and {high}.")
                continue
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
            continue

        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            score = max(100 - (attempts - 1) * 10, 10)
            print(f"✅ Correct! You guessed it in {attempts} attempts.")
            print(f"🏆 Your score: {score} points.\n")
            break


def main():
    """Main loop allowing multiple rounds."""
    while True:
        play_game()
        again = input("Would you like to play again? (y/n): ").lower().strip()
        if again != "y":
            print("\n👋 Thanks for playing Guess the Number!")
            break


if __name__ == "__main__":
    main()
