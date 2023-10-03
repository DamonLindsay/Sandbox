"""
Seminar Activity
"""

names = ["Ada", "Alan", "Bill", "John"]
print(", ".join(names))

name_to_remove = input("Who do you want to remove? ")
while name_to_remove != "":
    try:
        names.remove(name_to_remove)
    except ValueError:
        print("No such name.")
    name_to_remove = input("Who do you want to remove? ")
print(", ".join(names))
