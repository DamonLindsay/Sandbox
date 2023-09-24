"""
Guessing Game Demo
"""
import random


def main():
    """This program is a guessing game, where a random number is generated the user attempts to guess it."""
    secret = random.randint(1, 10)
    guess = int(input("Guess: "))
    while guess != secret:
        print("Incorrect guess.")
        guess = int(input("Guess: "))
    print("You got it!")


main()
