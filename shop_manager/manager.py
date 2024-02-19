"""
Manager class file
"""

from employee import Employee


class Manager(Employee):
    """Class representing a manager."""

    def __init__(self, name, employee_id, salary, bonus):
        """Initializes a Manager object."""
        super().__init__(name, employee_id)
        self.salary = salary
        self.bonus = bonus

    def calculate_pay(self):
        """Calculates the pay of the manager."""
        return self.salary + self.bonus
