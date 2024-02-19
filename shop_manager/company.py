"""
Company Class File
"""
from employee import HourlyEmployee, SalariedEmployee, Manager, Executive


class Company:
    """Class representing a company."""

    def __init__(self):
        """Initializes a Company object with an empty list of employees."""
        self.employees = []

    def hire_employee(self, employee):
        """Hires an employee and adds them to the list of employees."""
        self.employees.append(employee)

    def fire_employee(self, employee):
        """Fires an employee and removes them from the list of employees."""
        self.employees.remove(employee)

    def raise_employee(self, employee, raise_amount):
        """Gives a raise to an employee."""
        if isinstance(employee, HourlyEmployee):
            employee.hourly_rate += raise_amount
        elif isinstance(employee, SalariedEmployee):
            employee.salary += raise_amount
        elif isinstance(employee, Manager):
            employee.bonus += raise_amount
        elif isinstance(employee, Executive):
            employee.stock_options += raise_amount
        else:
            raise ValueError("Invalid employee type.")
