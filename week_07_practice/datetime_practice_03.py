"""
Generating a Date String in a Specific Format
This code illustrates how to format a date as a string in a custom
format using the 'strftime' method from the 'datetime' module.  In this case, it shows the date in the format "Day of
the Week, Month, Day, Year.
"""

import datetime

today = datetime.date.today()
formatted_date = today.strftime("%A, %B, %d, %Y")
print(f"Formatted date: {formatted_date}")
