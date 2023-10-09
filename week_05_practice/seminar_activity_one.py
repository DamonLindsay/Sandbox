"""
Seminar Activity One

Write code for a function that takes two lists: a list of names, and a corresponding list of ages. Elements at the same
list index represent the same person. The function will return the name of the oldest person in the list. If multiple
people have the same oldest age, return the first name.
"""


def main():
    """This program will """
    names = ["Bill", "Jane", "Sven"]
    ages = [21, 34, 56]
    print(find_oldest(names, ages))


def find_oldest(names, ages):
    """Return the name of the oldest person in the list."""
    # return names[ages.index(max(ages))]
    oldest_age = -1
    oldest_index = -1
    for i, age in enumerate(ages):
        if age > oldest_age:
            oldest_age = age
            oldest_index = i
    return names[oldest_index]


def run_tests():
    """Return the name of the oldest person in the list."""
    i = 0
    names = ["Bill", "Jane", "Sven", "Max"]
    ages = [21, 34, 56, 0]
    print(f"{names[i]} is {ages[i]} years old.")


main()
# run_tests()
