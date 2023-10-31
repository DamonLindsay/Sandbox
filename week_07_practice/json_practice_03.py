"""
Handling JSON with Complex Data Structures
This example showcases how to serialize and deserialize a complex data structure (a list of dictionaries) into JSON
using 'json.dumps' and 'json.loads'.
"""
import json

# Complex data structure: List of Dictionaries
employees = [{"name": "Alice", "age": 25, "department": "HR"}, {"name": "Bob", "age": 30, "department": "Engineering"},
             {"name": "Charlie", "age": 35, "department": "Marketing"}]

# Serializing complex data to JSON
json_data = json.dumps(employees)
print(f"Serialized JSON data: {json_data}")

# Deserializing JSON data to complex Python data structure
original_data = json.loads(json_data)
print(f"Deserialized JSON data: {original_data}")
