"""
Write code to prompt the user for a new name and age, add these to the dictionary,
then display all the data nicely.
"""

name_to_age = {"Bill": 21, "Jane": 4, "Sven": 56}

name = input("Name: ")
age = int(input("Age: "))

name_to_age[name] = age
max_length = max(len(name) for name in list(name_to_age.keys()))

for name, age in name_to_age.items():
    print(f"{name:{max_length}} - {age:4}")
