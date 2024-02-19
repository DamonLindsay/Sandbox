"""
Executive Class File
"""

from employee import Employee


class Executive(Employee):
    """Class representing an executive."""
    def __init__(self, name, employee_id, salary, stock_options):
        """Initializes an Executive object."""
        super().__init__(name, employee_id)
        self.salary = salary
        self.stock_options = stock_options

    def calculate_pay(self):
        """Calculates the pay of the executive."""
        return self.salary + self.stock_options
