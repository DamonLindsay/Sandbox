"""Person V2"""


class Person:
    """Person class"""

    def __init__(self, name, age):
        """Initialize the person class."""
        self.name = name
        self.age = age

    def __str__(self):
        """Return the string version of the Person class."""
        return f"{self.name} ({self.age})"

    def __repr__(self):
        """Return the """
        return f"{self.name} ({self.age})"

    def __eq__(self, other):
        """Return True if the name and age of the comparison are the same."""
        return self.name == other.name and self.age == other.age


p1 = Person("Jane", 19)
p2 = Person("Jane", 19)
p3 = Person("Bob", 24)
# print(p1)
# people = [Person("Alexa", 21), Person("Siri", 25)]
# print(people)

print(f"Person 1: {p1}")
print(f"Person 2: {p2}")
print(f"Person 3: {p3}")

print(f"Expected: True, Actual: {p1 == p2}")
print(f"Expected: False, Actual: {p1 == p3}")
