"""
Guessing Game Demo
"""
FILENAME = "secret.txt"


def main():
    """This program is a guessing game, where a random number is generated the user attempts to guess it."""
    secret = load_number(FILENAME)

    guess = get_valid_integer()
    while guess != secret:
        print("Incorrect guess.")
        guess = get_valid_integer()
    print("You got it!")


def get_valid_integer():
    """Get a valid integer from the user."""
    is_valid_input = False
    while not is_valid_input:
        try:
            guess = int(input("Guess: "))
            is_valid_input = True
        except ValueError:
            print("Invalid integer.")
    return guess  # No problem with potential undefined variable.


def load_number(filename):
    """Load an integer from file filename."""
    try:
        infile = open(filename, "r")
        number = int(infile.read())
    except ValueError:
        print(f"Invalid contents in file '{filename}'.")
        number = 6
    except FileNotFoundError:
        print(f"'{filename}' not found.")
        number = 4
    else:
        infile.close()
    return number


main()
