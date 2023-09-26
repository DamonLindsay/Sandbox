"""
Seminar 03 Practice
"""

# filename = input("Please enter data file: ")
#
# with open("practice_data.txt", "r") as in_file:
#     for line in in_file:
#         if line[0] == "#":
#             print(line.strip())


# name = input("Name: ")
#
# with open("name.txt", "w") as out_file:
#     print(name, file=out_file)

# Version 1
strings = ["test01", "test02", "test03", "blah"]
# for string in strings:
#     with open(f"{string}.txt", "w") as out_file:
#         print(string, file=out_file)

for string in strings:
    try:
        with open(f"{string}.txt", "r") as out_file:
            print(string)
    except FileNotFoundError:
        print(f"Error: '{string}.txt' - File was not found.")

value = int(input("> "))
result = f"{value}" * value
thing = result[value]
