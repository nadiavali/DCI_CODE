from datetime import datetime
from sqlite3 import Timestamp

# For a portable representation of datetime obj

time_1 = datetime(day=14, month=6, year=2022, hour= 9, minute=0)

# timestamps, also known as UNIX timestamp
# measures the time in milliseconds since Jan 1 1970

timestamp = datetime.timestamp(time_1)

print(f'Timestamp: {timestamp}')

time_2 = datetime.fromtimestamp(timestamp)

print(time_2.year, time_2.month)