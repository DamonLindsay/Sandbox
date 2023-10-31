"""
Calculating the Difference Between Two Dates
This program demonstrates how to find the difference between two specific dates using the 'datetime' module.
"""

import datetime

date_1 = datetime.datetime(2023, 5, 15)
date_2 = datetime.datetime(2023, 10, 31)

time_difference = date_2 - date_1
print(f"Difference between dates: {time_difference}")
