"""
Customer Class File
"""
import random


class Customer:
    """Class representing a customer."""

    def __init__(self, name):
        """Initializes a Customer object."""
        self.name = name

    def make_purchase(self):
        """Simulates a customer making a purchase and returns the sale amount."""
        return random.randint(1, 1000)  # Random sale amount
