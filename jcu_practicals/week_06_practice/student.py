"""Student"""


class Student:
    def __init__(self, first_name="", last_name="", student_id=0):
        self.first_name = first_name
        self.last_name = last_name
        self.id = student_id

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.id})"


# Simple example class usage (client code):
first_name = input("First name: ")
last_name = input("Last name: ")
student_id = int(input("Student ID: "))
s1 = Student(first_name, last_name, student_id)
print(f"{s1.first_name} has ID {s1.id} ")
