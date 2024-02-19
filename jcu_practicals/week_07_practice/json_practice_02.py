"""
Reading and Writing JSON to a File
This program showcases how to write JSON data to a file using 'json.dump' and then read JSON data from the file using
'json.load'.
"""
import json

# Sample data to write to a JSON file
data = {"name": "Alice", "age": 28, "city": "San Francisco"}

# Writing JSON data to a file
with open("data.json", "w") as input_file:
    json.dump(data, input_file)

# Reading JSON data from the file
with open("data.json", "r") as output_file:
    loaded_data = json.load(output_file)
    print(f"Loaded data from file: {loaded_data}")
