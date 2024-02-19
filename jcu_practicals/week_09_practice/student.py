"""
Student class module
"""
from jcu_practicals.week_09_practice.person import Person


class Student(Person):
    def __init__(self, student_id: int, course: str, **kwargs):
        super().__init__(**kwargs)
        self.id = student_id
        self.course = course

    def __repr__(self):
        return str(vars(self))


    def __str__(self):
        return f"{super().__str__()} ID: {self.id}, Course: {self.course}"
