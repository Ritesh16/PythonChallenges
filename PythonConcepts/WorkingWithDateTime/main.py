import datetime as dt

now = dt.datetime.now()

year = now.year
month = now.month
day = now.day
print(f"{year}/{month}/{day}")
print(now)

# creating a date
date = dt.datetime(year=1988, month=9, day=16)
print(date)

