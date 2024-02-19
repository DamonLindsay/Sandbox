"""
Seminar Activities Challenge
"""

import csv


def main():
    """This program will print the data found in countries.csv."""
    filename = "countries.csv"
    countries_data = load_countries_data(filename)
    display_formatted_data(countries_data)


def load_countries_data(filename):
    """Load the countries data from the file."""
    data = []
    with open(filename, "r") as in_file:
        csv_reader = csv.reader(in_file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            country, capital, population, percentage, _ = row
            population = int(population.replace(",", ""))
            percentage = float(percentage.rstrip("%"))
            data.append((country, capital, population, percentage))
    return data


def display_formatted_data(data):
    """Display the formatted and sorted data."""
    data.sort(key=lambda x: x[0])  # Sort the data by country name
    max_country_name_length = max(len(country) for country, _, _, _ in data)
    max_capital_name_length = max(len(capital) for _, capital, _, _ in data)
    max_population_length = max(len(population) for _, _, population, _ in data)
    max_percentage_length = max(len(percentage) for _, _, _, percentage in data if percentage)
    for country, capital, population, percentage in data:
        print(f"{country:<{max_country_name_length}} - {capital:<{max_capital_name_length}} "
              f"{population:<{max_population_length}} {percentage:>{max_percentage_length}.2f}%")


main()
