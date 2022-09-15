from datetime import datetime, date
import calendar

now = datetime.now()

# current_time = print(now.strftime('%H:%M:%S'))

# Task1
current_year =print(datetime.now().year)

# Task2
weekday_week = print(calendar.weekday(2022, 1, 10))

# Task3
if calendar.isleap(2021):
    print('2021 is a leap year!')
else:
    print('2021 is not a leap year!')
# Task4
date_as_str= 'Feb 14 2021 8:30AM'
print("type of date_as_str =", type(date_as_str))
convert_date = datetime.strptime(date_as_str, '%b %d %Y %I:%M%p')

print(convert_date)