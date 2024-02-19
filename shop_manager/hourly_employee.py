"""
Hourly Employee class
"""

from employee import Employee


class HourlyEmployee(Employee):
    """Class representing an hourly employee."""

    def __init__(self, name, employee_id, hours_worked, hourly_rate):
        """Initializes an HourlyEmployee object."""
        super().__init__(name, employee_id)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_pay(self):
        """Calculates the pay of the hourly employee."""
        return self.hours_worked * self.hourly_rate
