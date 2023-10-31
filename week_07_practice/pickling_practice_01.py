"""
Pickling and Unpicking a Python Object
This program demonstrates how to pickle a Python object into a binary file using 'pickle.dump' and then unpickle the
object back using 'pickle.load'.
"""
import pickle

# Object to pickle
data = {"name": "Alice", "age": 30, "city": "New York"}

# Pickling the object
with open("data.pkl", "wb") as input_file:
    pickle.dump(data, input_file)

# Unpickling the object
with open("data.pkl", "rb") as output_file:
    loaded_data = pickle.load(output_file)
    print(f"Unpickled data: {loaded_data}")
