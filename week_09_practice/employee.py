"""
Employee class module
"""

from person import Person


class Employee(Person):
    def __init__(self, salary: float, **kwargs):
        super().__init__(**kwargs)
        self.salary = salary

    def __repr__(self):
        return str(vars(self))
