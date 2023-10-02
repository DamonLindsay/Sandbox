"""
Seminar activity.
"""


# Write a program that contains a (hard-coded) list of names. Ask the user which name they
# want to display as a number (1 = first name in the list), and then display it. Avoid any
# IndexError by using exception handling.
def main():
    """This program will ask the user which name they want to display as a number, then display it."""
    names = ["Damon", "Camryn", "Liam", "Maddison", "Noah", "Natalie", "Craig", "Jordan"]

    number = int(input("Enter number, up to 8: "))

    print(names[number])


main()
