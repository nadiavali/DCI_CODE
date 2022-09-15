import calendar
from datetime import datetime
# set first day of week to Saturday 0=Monday 6= sunday
calendar.setfirstweekday(5)

# print(calendar.firstweekday())

print(calendar.month(2021, 1))

time_1 = datetime(day=14, month=6, year=2022, hour= 9, minute=0)

# print(calendar.isleap(2024))
#get datetime obj and check if year is a leap year (sal kabise)

print(calendar.isleap(time_1.year))