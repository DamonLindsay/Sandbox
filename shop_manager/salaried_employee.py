"""
Salaried Employee class file
"""
from employee import Employee


class SalariedEmployee(Employee):
    """Class representing a salaried employee."""

    def __init__(self, name, employee_id, salary):
        """Initializes a SalariedEmployee object."""
        super().__init__(name, employee_id)
        self.salary = salary

    def calculate_pay(self):
        """Calculates the pay of the salaried employee."""
        return self.salary
