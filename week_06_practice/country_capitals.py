"""Demo - country: capital city loaded from CSV."""

import csv

FILENAME = "../week_05_practice/countries.csv"


def main():
    country_to_capital = load_data(FILENAME)
    print(country_to_capital)


def load_data(filename):
    country_to_capital = {}
    with open(filename, "r") as input_file:
        input_file.readline()  # Ignore CSV header line
        reader = csv.reader(input_file)
        for row in reader:
            row[2] = int(row[2].replace(",", ""))
            row[3] = float(row[3][:-1])
            row[4] = int(row[4][-4:])
            print(row)

            input()
        # for line in input_file:
        #     parts = line.split(",")
        #     print(parts)

    return country_to_capital


main()
