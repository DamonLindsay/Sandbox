"""
Pickling Custom Objects
In this example, a custom class 'Person' is pickled and then unpickled to demonstrate how to serialize and
deserialize custom objects using 'pickle'.
"""
import pickle


# Define a simple class
class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age


# Create an instance of the class
person = Person("Bob", 25)

# Pickling the custom object
with open("person.pkl", "wb") as input_file:
    pickle.dump(person, input_file)

# Unpickling the object
with open("person.pkl", "rb") as output_file:
    loaded_person = pickle.load(output_file)
    print(f"Unpickled Person object - Name: {loaded_person.name}, Age: {loaded_person.age}.")
