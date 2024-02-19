"""datetime - Basic date and time types."""

import datetime

d1 = datetime.date(2022, 11, 3)
print(type(d1))
print(d1.isoweekday())
print(d1.strftime("%d...%m"))
print(d1.strftime("%d...%B"))
print(d1.strftime("%d...%B - (%A)"))
print(d1.strftime("%d/%m/%y"))
print(d1.strftime("%d/%m/%yyyy"))
print(d1.strftime("%d/%m/%yy"))
print(d1.strftime("%d/%m/%Y"))
print(d1.strftime("%d of %B (which is a %A)"))

print(d1.month)
print(d1.year)

d2 = datetime.date(2022, 12, 25)
print(d2.isoweekday())
print(d2.weekday())
print(d2.strftime("%A"))
days_to_go = d2 - d1
# days_to_go - 1  <-- Won't work, not an object
print(days_to_go.days)
print(type(days_to_go.days))
print(days_to_go.days - 1)

s = "11/9/1980"
print(s)
print(s.split("/"))
print([int(part) for part in s.split("/")])
values = [int(part) for part in s.split("/")]
print(datetime.datetime.strptime(s, "%d/%m/%Y"))

d3 = datetime.date(values[2], values[1], values[0])
print(d3)


