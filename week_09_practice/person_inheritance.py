"""
Person Inheritance module
"""
from person import Person
from student import Student
from employee import Employee
from datetime import datetime
from musician import Musician

if __name__ == '__main__':
    p1 = Person("Jane", datetime(1999, 2, 14))
    print(p1)
    print(p1.age())
    print()
    s1 = Student(name="Jerry", date_of_birth=datetime(2001, 12, 14), student_id=12345, course="BIT")
    print(s1)
    print(s1.age())
    print(s1.course)
    print(s1.id)
    print()
    e1 = Employee(name="Maddison", date_of_birth=datetime(1995, 1, 30), salary=80000)
    print(e1)
    print(e1.age())
    print(e1.salary)
    print()
    m1 = Musician(name="David", date_of_birth=datetime(1967, 11, 7), style="Dance/Electronic")
    print(m1)
    print(m1.age())
    print(m1.style)
    print(m1.play(60))
