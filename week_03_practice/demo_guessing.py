"""
Guessing Game Demo
"""
FILENAME = "secret.txt"


def main():
    """This program is a guessing game, where a random number is generated the user attempts to guess it."""
    secret = load_number(FILENAME)
    guess = int(input("Guess: "))
    while guess != secret:
        print("Incorrect guess.")
        guess = int(input("Guess: "))
    print("You got it!")


def load_number(filename):
    """Load an integer from file filename."""
    infile = open(filename, "r")
    number = int(infile.read())
    infile.close()
    return number


main()
