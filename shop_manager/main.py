from employee import Employee
from hourly_employee import HourlyEmployee
from salaried_employee import SalariedEmployee
from manager import Manager
from executive import Executive
from company import Company
from customer import Customer


def main():
    """FIX THIS"""
    # Create employees
    hourly_employee = HourlyEmployee("John", 1, 40, 15)
    salaried_employee = SalariedEmployee("Alice", 2, 50000)
    manager = Manager("Bob", 3, 70000, 5000)
    executive = Executive("Eve", 4, 100000, 10000)

    # Create company
    company = Company()
    company.hire_employee(hourly_employee, 2)
    company.hire_employee(salaried_employee, 1000)
    company.hire_employee(manager, 2000)
    company.raise_employee(executive, 5000)

    # Display initial salaries
    print("Initial salaries: ")
    for employee in company.employees:
        print(f"{employee.name}: {employee.calculate_pay()}")

    # Give raises
    company.raise_employee(hourly_employee, 2)
    company.raise_employee(salaried_employee, 1000)
    company.raise_employee(manager, 2000)
    company.raise_employee(executive, 5000)

    # Display salaries after raises
    print(f"\nAfter raises:")
    for employee in company.employees:
        print(f"{employee.name}: {employee.calculate_pay()}")

    # Simulate customers
    customers = [Customer("Customer 1"), Customer("Customer 2"), Customer("Customer 3")]
    for customer in customers:
        sale_amount = customer.make_purchase()
        print(f"{customer.name} made a purchase of ${sale_amount}")


if __name__ == '__main__':
    main()
