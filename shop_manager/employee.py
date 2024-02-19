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


class SalariedEmployee(Employee):
    """Class representing a salaried employee."""

    def __init__(self, name, employee_id, salary):
        """Initializes a SalariedEmployee object."""
        super().__init__(name, employee_id)
        self.salary = salary

    def calculate_pay(self):
        """Calculates the pay of the salaried employee."""
        return self.salary


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

    def __str__(self):
        """Returns a string representation of the Manager object."""
        return f"Manager {self.name}, Employee ID: {self.id}, Salary: {self.salary}, Bonus: {self.bonus}"


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
