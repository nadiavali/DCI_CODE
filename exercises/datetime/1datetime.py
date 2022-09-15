from datetime import datetime, date

print(datetime.today())

date_as_string = '2022-01-10'
print(date.fromisoformat(date_as_string))

date = "10 January 1993"  # Converting str into datetime object
converted_date = datetime.strptime(date, "%d %B %Y") # The date format and the format of strptime should be the same and the result will be as ISO 8601
print(converted_date)

print(datetime.now().strftime('%H:%M:%S'))
# Changing the format of the obj
# useful for cherryPicking specific of the datetime obj
print(converted_date.strftime('%Y-%m-%d %H:%M:%S'))


date = 'March 28 2011, 16:12'
convert_date = datetime.strptime(date, '%B %d %Y, %H:%M')
print(convert_date)

year = convert_date.year
year += 2
print(year)