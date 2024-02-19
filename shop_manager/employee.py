"""
Employee Class
"""

from abc import ABC, abstractmethod


class Employee(ABC):
    """Abstract base class representing an employee."""

    def __init__(self, name, employee_id):
        """Initializes an Employee object."""
        self.name = name
        self.id = employee_id

    @abstractmethod
    def calculate_pay(self):
        """Abstract method to calculate the pay of the employee."""
        pass
