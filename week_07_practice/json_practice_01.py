"""
Serializing and Deserializing JSON Data
This program demonstrates how to convert a Python dictionary into a JSON string using 'json.dumps' and then convert
the JSON string back into a python dictionary using 'json.loads'.
"""
import json

# Example JSON data
data = {"name": "John Doe", "age": 30, "city": "New York"}

# Serializing Python dictionary to JSON
json_data = json.dumps(data)
print(f"Serialized JSON data: {json_data}")

# Deserializing JSON data to Python Dictionary
original_data = json.loads(json_data)
print(f"Deserialized JSON data: {original_data}")
