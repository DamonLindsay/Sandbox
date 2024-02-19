"""Demo - country: capital city loaded from CSV."""

import csv
from jcu_practicals.week_06_practice.city import City

FILENAME = "../week_05_practice/countries.csv"


def main():
    """Countries from CSV program."""
    country_to_capital = load_data(FILENAME)
    # print(country_to_capital)
    print("Welcome.  What do you want?")
    while True:
        country = input("Country: ")
        try:
            print(country_to_capital[country])
            break
        except KeyError:
            print("Invalid country.")
    print("Finished.")


def load_data(filename):
    """Load CSV data as dictionary of country: City object."""
    country_to_capital = {}
    with open(filename, "r") as input_file:
        input_file.readline()  # Ignore CSV header line
        reader = csv.reader(input_file)
        for row in reader:
            row[2] = int(row[2].replace(",", ""))
            row[3] = float(row[3][:-1])
            # row[4] = int(row[4][-4:])
            # print(row)
            city = City(row[1], row[2], row[3])
            # print(city)
            country_to_capital[row[0]] = city
    return country_to_capital


main()
