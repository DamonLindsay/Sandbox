"""
Student class module
"""
from week_09_practice.person import Person


class Student(Person):
    def __init__(self, student_id: int, course: str, **kwargs):
        super().__init__(**kwargs)
        self.id = student_id
        self.course = course

    def __repr__(self):
        return str(vars(self))
