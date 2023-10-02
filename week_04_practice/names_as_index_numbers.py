"""
Seminar activity.
"""


# Write a program that contains a (hard-coded) list of names. Ask the user which name they
# want to display as a number (1 = first name in the list), and then display it. Avoid any
# IndexError by using exception handling.
def main():
    """This program will ask the user which name they want to display as a number, then display it."""
    names = ["Damon", "Camryn", "Liam", "Maddison", "Noah", "Natalie", "Craig", "Jordan"]

    selected_name = get_name_by_number(names)
    print(selected_name)


def get_name_by_number(sequence):
    """Return the name of the specified index - 1."""
    is_valid_input = False
    while not is_valid_input:
        try:
            number = int(input(f"Enter number, up to {len(sequence)}: "))
            if number <= 0:
                print("Invalid number.  Number must be greater than 0.")
            else:
                is_valid_input = True
                return sequence[number - 1]
        except IndexError:
            print("IndexError. List index out of range.")


main()
