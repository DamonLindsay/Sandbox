"""
Pickling and Unpickling Lists and Dictionaries
This program illustrates pickling and unpickling a list and a dictionary using 'pickle.dump' and 'pickle.load'.
"""
import pickle

# Pickling a list
data_list = [1, 2, 3, 4, 5]
with open("data_list.pkl", "wb") as input_file:
    pickle.dump(data_list, input_file)

# Unpickling the list
with open("data_list.pkl", "rb") as output_file:
    loaded_list = pickle.load(output_file)
    print(f"Unpickled list: {loaded_list}")

# Pickling a dictionary
data_dict = {"a": 1, "b": 2, "c": 3}
with open("data_dict.pkl", "wb") as input_file:
    pickle.dump(data_dict, input_file)

# Unpickling the dictionary
with open("data_dict.pkl", "rb") as output_file:
    loaded_dict = pickle.load(output_file)
    print(f"Unpickled dictionary: {loaded_dict}")
