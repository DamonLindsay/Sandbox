from employee import Employee, HourlyEmployee, SalariedEmployee, Manager, Executive
from company import Company
from customer import Customer
import random

FIRST_NAME_FILE = "first_names.txt"


def main():
    company = Company()

    # Create and add one manager to the company
    manager_name = get_random_name_from_file(FIRST_NAME_FILE)
    manager = Manager(manager_name, 1, 1000, 200)
    company.hire_employee(manager)

    print("Welcome to the Shop Manager Simulator!")
    display_instructions()
    choice = input("Please enter your choice: ").lower()
    while choice != "q":
        if choice == "i":
            display_instructions()
        elif choice == "s":
            print("\nSimulating day...")
            # MORE HERE
            for employee in company.employees:
                print(employee)
            print()
        elif choice == "q":
            print("\nExiting program...")
            break
        else:
            print("\n Invalid choice.  Please try again.")
        choice = input("Please enter your choice: ").lower()


def display_instructions():
    """FIX"""
    print("Menu options:")
    print("i - Display instructions")
    print("s - Simulate day")
    print("q - Quit")


def get_random_name_from_file(filename):
    """FIX"""
    with open(filename, "r") as input_file:
        names = input_file.readlines()
        return random.choice(names).strip()


if __name__ == '__main__':
    main()
