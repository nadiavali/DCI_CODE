from datetime import datetime

# print(datetime.today())

# date_as_string = '2022-01-10'
# print(date.fromisoformat(date_as_string))

date = "10 January 1993"
converted_date = datetime.strptime(date, "%d %B %Y") # The date format and the format of strptime should be the same and the result will be as ISO 8601
print(converted_date)

