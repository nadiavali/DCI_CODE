from datetime import datetime, timedelta
# Calculate difference between 2 times
time_1 = datetime(day=14, month=6, year=2022, hour= 9, minute=0)
time_2 = datetime(day=14, month=6, year=2022, hour= 16, minute=15)

difference = time_2 - time_1

print(difference)

#  calculate a time in future


time_3 = datetime(day=14, month=6, year=2022, hour= 16, minute=15)
# days= # hours= # minuets= # microseconds=
print(time_3 + timedelta(hours=46))