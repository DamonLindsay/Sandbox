"""
Person class module
"""
from datetime import datetime


class Person:
    """Class of a person."""

    def __init__(self, name: str, date_of_birth: datetime.date):
        """Initialize the person object."""
        self.name = name
        self.date_of_birth = date_of_birth

    def __repr__(self):
        date_string = datetime.strftime(self.date_of_birth, "%d/%m/%Y")
        return f"{self.name} ({date_string})"

    def age(self):
        return int((datetime.now() - self.date_of_birth).days / 365.2425)
