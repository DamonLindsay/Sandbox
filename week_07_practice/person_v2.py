"""Person V2"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

    def __repr__(self):
        return f"{self.name} ({self.age})"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


p1 = Person("Jane", 19)
p2 = Person("Jane", 19)
p3 = Person("Bob", 24)
print(p1)
people = [Person("Alexa", 21), Person("Siri", 25)]
print(people)

is_same = p1 == p2
is_not_same = p1 == p3
print(is_same)
print(is_not_same)

