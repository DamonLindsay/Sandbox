"""
Practice With Files
"""

with open("data.txt", "r") as in_file:
    for line in in_file:
        parts = line.strip().split(',')
        name = parts[0]
        year = int(parts[1])
        price = float(parts[2])
        print(f"{name} was created in {year} and is currently worth ${price:.2f}.")
