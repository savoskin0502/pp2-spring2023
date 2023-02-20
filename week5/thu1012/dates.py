import datetime


date1 = datetime.datetime(year=2023, month=2, day=16)
date2 = datetime.datetime(year=1977, month=6, day=5)

print(date1, type(date1))
print(date2 == date1)
print(date2 - date1)
print(type(date2 - date1))

delta_day = datetime.timedelta(hours=12, days=1)
print(date1 + delta_day)  # datetime.datetime

print(date1.strftime('%B %Y'))

datetime_string = 'February:2023'
new_date = datetime.datetime.strptime(datetime_string, '%B:%Y')
print(new_date, 'new_date', type(new_date))
# date -> YYYY-MM-DD
# time -> h24-m-mm
