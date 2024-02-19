"""Person"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

    def __repr__(self):
        return f"{self.name} ({self.age})"


p1 = Person("Jane", 19)
print(p1)
people = [Person("Alexa", 21), Person("Siri", 25)]
print(people)
