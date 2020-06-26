"""
Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.

"""

import calendar

try:
    year = int(input("Input a year: "))
    month = int(input("Input a month: "))
    print(calendar.month(year,month))

except:
    print("Please, put a valid format")